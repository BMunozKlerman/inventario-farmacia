#!/usr/bin/env python3
"""Pipeline 7Cs: PDF -> COM -> mapping -> composición -> auditoría -> slice backend."""

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from sevencs import render
from sevencs.agent import AgentNotAvailable, check_login, load_registry, run_prompt, select_profile
from sevencs.audit import AuditFailed, ClarificationGateClosed, audit
from sevencs.clarifications import read_open_questions, request_answers
from sevencs.paths import REPO_ROOT, PathOutsideRepo, repo_path, resolve_pdf
from sevencs.skills import inline_skills

STAGE_DIRECTORIES = ("evidence", "com", "mapping", "composed", "audit", "clarifications")
READING_SKILLS = (
    "7cs-canvas-ingest", "7cs-business-context", "7cs-architectural-context",
    "7cs-system-context", "7cs-structural", "7cs-functional-A", "7cs-functional-B",
    "7cs-deployment",
)
TRANSFORM_SKILLS = ("7cs-com-transform",)
COMPOSE_SKILLS = ("7cs-spec-compose",)
BACKEND_SKILLS = ("7cs-backend-slice",)
CANVAS_KEYS = (
    "business_context", "architectural_context", "system_context", "structural",
    "functional_front", "functional_back", "deployment",
)
ENCODING_RULE = (
    "Lee y escribe todos los archivos como UTF-8; conserva tildes, eñes y signos de apertura."
)


def parse_arguments(argv):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pdf-path", required=True)
    parser.add_argument("--delivery-id", required=True)
    parser.add_argument("--budget-path", default="config/com-budget.json")
    parser.add_argument("--keep-existing", action="store_true")
    parser.add_argument("--com-only", action="store_true")
    arguments = parser.parse_args(argv)
    if not re.fullmatch(r"[A-Za-z0-9_-]+", arguments.delivery_id):
        parser.error("--delivery-id sólo admite letras, dígitos, guion y guion bajo")
    return arguments


def prepare_directories(root, delivery_id, keep_existing):
    for name in STAGE_DIRECTORIES:
        directory = repo_path(root, name)
        directory.mkdir(parents=True, exist_ok=True)
        if keep_existing:
            continue
        for stale in directory.glob("{}-*".format(delivery_id)):
            if stale.is_file():
                stale.unlink()


def validate_budget(root, delivery_id, budget_path):
    with open(repo_path(root, budget_path), encoding="utf-8") as handle:
        budget = json.load(handle)

    counts = {key: 0 for key in CANVAS_KEYS}
    sticky_ids = []
    com_files = sorted(repo_path(root, "com").glob("{}-*.json".format(delivery_id)))
    if not com_files:
        raise RuntimeError("El agente no generó COM")

    for path in com_files:
        with open(path, encoding="utf-8") as handle:
            com = json.load(handle)
        key = "functional_{}".format(com.get("variant")) if com.get("canvas") == "functional" \
            else com.get("canvas")
        if key in counts:
            counts[key] += 1
        for section in com.get("sections") or []:
            for sticky in section.get("stickies") or []:
                if not sticky.get("id") or not sticky.get("text") or len(sticky.get("bbox") or []) != 4:
                    raise RuntimeError("Post-it inválido en {}".format(path.name))
                sticky_ids.append(sticky["id"])

    for name, expected in budget.items():
        print("  {}: {}/{}".format(name, counts.get(name, 0), expected))
        if counts.get(name, 0) != int(expected):
            raise RuntimeError("Presupuesto COM incumplido: {}".format(name))

    if len(set(sticky_ids)) != len(sticky_ids):
        raise RuntimeError("Existen IDs de post-it duplicados")
    print("  post-its: {}".format(len(sticky_ids)))


def main(argv=None):
    arguments = parse_arguments(argv)
    root = REPO_ROOT
    delivery_id = arguments.delivery_id

    pdf = resolve_pdf(root, arguments.pdf_path)
    registry = load_registry(repo_path(root, "config/agents.json"))
    profile, executable = select_profile(registry)
    check_login(profile, executable)
    print("Agente de IA: {} ({})".format(profile.name, executable))
    render.find_renderer()

    prepare_directories(root, delivery_id, arguments.keep_existing)
    skills_root = repo_path(root, ".agents/skills")

    def invoke(skills, prompt, images=()):
        run_prompt(profile, executable, inline_skills(skills_root, skills) + "\n" + prompt,
                   root, images)

    print("[1/7] Renderizando el PDF localmente")
    evidence = repo_path(root, "evidence")
    pages = render.render_pages(pdf, evidence, delivery_id, root=root)
    render.write_page_index(pdf, evidence, delivery_id, pages)
    images = sorted(evidence.glob("{}-p*.png".format(delivery_id)))

    print("[2/7] Leyendo canvas y generando COM")
    answers_path = repo_path(root, "clarifications/{}-answers.json".format(delivery_id))
    reading_questions = repo_path(root, "clarifications/{}-reading.json".format(delivery_id))
    reading_prompt = """Procesa el delivery '{delivery}' desde las imágenes del PDF resources/{pdf}. Aplica 7cs-canvas-ingest y entrega cada candidato a los siete lectores locales. Genera exclusivamente COM literales en com/ e informe e índice en evidence/. {encoding} No transformes, compongas ni audites.

Escribe siempre clarifications/{delivery}-reading.json con {{"delivery_id":"{delivery}","phase":"reading","questions":[]}}. Ante texto ilegible, clasificación insegura o datos imprescindibles ambiguos, agrega preguntas concretas con {{"id","question","reason","status":"open"}}, usa ids estables Q-READ-NNN y no adivines. Si existen respuestas en clarifications/{delivery}-answers.json, analízalas junto con la imagen: marca la pregunta resolved sólo si la respuesta permite una transcripción o clasificación inequívoca; de lo contrario mantenla open y reformúlala.

No modifiques resources/, .agents/, scripts/, config/, tests/, README.md ni AGENTS.md.""".format(
        delivery=delivery_id, pdf=pdf.name, encoding=ENCODING_RULE
    )
    invoke(READING_SKILLS, reading_prompt, images)
    while True:
        pending = read_open_questions(reading_questions)
        if not pending:
            break
        request_answers(answers_path, delivery_id, "reading", pending)
        invoke(READING_SKILLS, reading_prompt, images)

    print("[3/7] Validando los COM presupuestados")
    validate_budget(root, delivery_id, arguments.budget_path)

    if arguments.com_only:
        print("[4/7] Transformación omitida")
        print("[5/7] Composición omitida")
        print("[6/7] Auditoría omitida")
        print("[7/7] PDF -> COM: PASS")
        return 0

    print("[4/7] Transformando COM con compuerta de aclaraciones")
    transformation_questions = repo_path(
        root, "clarifications/{}-transformation.json".format(delivery_id)
    )
    transform_prompt = """Procesa el delivery '{delivery}' usando 7cs-com-transform. Lee únicamente com/{delivery}-*.json y, si existe, clarifications/{delivery}-answers.json. {encoding} Genera o reemplaza los artefactos mapping/{delivery}-*; no leas el PDF ni evidence/ y no compongas todavía.

Escribe siempre clarifications/{delivery}-transformation.json con {{"delivery_id":"{delivery}","phase":"transformation","questions":[]}}. Toda decisión ausente que impida requisitos verificables debe ser una pregunta concreta {{"id","question","reason","status":"open"}} con id estable Q-TRANS-NNN. Analiza cada respuesta contra los COM: marca resolved sólo si es suficiente; si no, mantén open y reformula la pregunta. No inventes. No continúes a composición.""".format(
        delivery=delivery_id, encoding=ENCODING_RULE
    )
    invoke(TRANSFORM_SKILLS, transform_prompt)
    while True:
        pending = read_open_questions(transformation_questions)
        if not pending:
            break
        request_answers(answers_path, delivery_id, "transformation", pending)
        invoke(TRANSFORM_SKILLS, transform_prompt)

    print("[5/7] Componiendo el entregable")
    invoke(COMPOSE_SKILLS, """Compone el delivery '{delivery}' mediante 7cs-spec-compose. Lee sólo mapping/{delivery}-*, clarifications/{delivery}-transformation.json y clarifications/{delivery}-answers.json. {encoding} Verifica que no existan preguntas open; si existe alguna, falla sin escribir composed/. Si la compuerta está cerrada, genera todos los artefactos composed/{delivery}-* y déjalos listos para 7cs-spec-audit. No leas el PDF ni evidence/.""".format(
        delivery=delivery_id, encoding=ENCODING_RULE
    ))

    print("[6/7] Ejecutando auditoría determinista")
    result = audit(
        delivery_id=delivery_id,
        com_directory=repo_path(root, "com"),
        mapping_directory=repo_path(root, "mapping"),
        clarification_directory=repo_path(root, "clarifications"),
        require_clarification_gate=True,
    )
    print("Audit {}: {} C={}".format(
        delivery_id, "PASS" if result.passed else "FAIL", result.coverage
    ))
    if not result.passed:
        return 1

    print("[7/7] Generando un slice backend ejecutable")
    invoke(BACKEND_SKILLS, """Usa 7cs-backend-slice para el delivery '{delivery}'. Selecciona exactamente un post-it Functional Back con contrato suficiente y genera un único bundle bajo implementation/{delivery}/backend-<capability>/. Debe incluir código fuente Node.js, pruebas sin dependencias innecesarias, Dockerfile, lanzadores multiplataforma run.sh y run.bat, README.md y traceability.json. Implementa solamente esa funcionalidad; no vuelvas al PDF, no cambies COM, mapping, composed ni clarifications y no generes frontend.""".format(
        delivery=delivery_id
    ))
    print("Pipeline completo: PASS")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (AgentNotAvailable, AuditFailed, ClarificationGateClosed, PathOutsideRepo,
            FileNotFoundError, RuntimeError, ValueError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        sys.exit(1)
