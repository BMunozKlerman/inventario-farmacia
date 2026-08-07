"""Auditoría determinista: cobertura de trazas y compuerta de aclaraciones."""

import json
from pathlib import Path

PHASES = ("reading", "transformation")


class AuditFailed(RuntimeError):
    pass


class ClarificationGateClosed(RuntimeError):
    pass


class AuditResult:
    def __init__(self, delivery_id, stickies, covered, coverage):
        self.delivery_id = delivery_id
        self.stickies = stickies
        self.covered = covered
        self.coverage = coverage
        self.passed = coverage == 1


def read_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def open_questions(clarification_directory, delivery_id):
    directory = Path(clarification_directory)
    questions = []
    for phase in PHASES:
        path = directory / "{}-{}.json".format(delivery_id, phase)
        if not path.is_file():
            raise ClarificationGateClosed(
                "Falta el archivo de aclaraciones {} para {}".format(path.name, delivery_id)
            )
        questions += [q for q in read_json(path).get("questions", []) if q.get("status") == "open"]
    return questions


def sticky_ids(com_directory, delivery_id):
    files = sorted(Path(com_directory).glob("{}-*.json".format(delivery_id)))
    if not files:
        raise AuditFailed("No hay COM para {}".format(delivery_id))
    ids = set()
    for path in files:
        for section in read_json(path).get("sections") or []:
            for sticky in section.get("stickies") or []:
                ids.add(sticky["id"])
    return ids


def traced_ids(mapping_directory, delivery_id, stickies):
    ids = set()
    for path in sorted(Path(mapping_directory).glob("{}-*-traces.json".format(delivery_id))):
        document = read_json(path)
        traces = document.get("traces", document) if isinstance(document, dict) else document
        for trace in traces or []:
            if trace.get("sticky_id") in stickies:
                ids.add(trace["sticky_id"])
    return ids


def audit(delivery_id, com_directory, mapping_directory, clarification_directory,
          require_clarification_gate=False, falsifiability_check=False):
    if require_clarification_gate:
        pending = open_questions(clarification_directory, delivery_id)
        if pending:
            raise ClarificationGateClosed(
                "Aclaraciones abiertas para {}: {}".format(delivery_id, len(pending))
            )

    stickies = sticky_ids(com_directory, delivery_id)
    traced = traced_ids(mapping_directory, delivery_id, stickies)
    covered = max(0, len(stickies) - 1) if falsifiability_check else len(traced)
    coverage = covered / len(stickies) if stickies else 1
    result = AuditResult(delivery_id, stickies, covered, coverage)

    if falsifiability_check and result.passed:
        raise AuditFailed("La prueba de falsabilidad no rechazó una traza faltante")
    return result
