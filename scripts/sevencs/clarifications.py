"""Compuerta de aclaraciones: lectura de preguntas abiertas y captura de respuestas por consola."""

import datetime
import json
from pathlib import Path


class AbortedByUser(RuntimeError):
    pass


def read_open_questions(path):
    path = Path(path)
    if not path.is_file():
        raise RuntimeError("El agente no generó el archivo de aclaraciones: {}".format(path))
    with open(path, encoding="utf-8") as handle:
        document = json.load(handle)
    return [q for q in document.get("questions", []) if q.get("status") == "open"]


def request_answers(answers_path, delivery_id, phase, questions, prompt=input):
    answers_path = Path(answers_path)
    responses = []
    if answers_path.is_file():
        with open(answers_path, encoding="utf-8") as handle:
            responses = json.load(handle).get("responses", [])

    print("")
    print("PIPELINE PAUSADO: se requieren {} aclaraciones ({}).".format(len(questions), phase))
    for question in questions:
        print("")
        print("[{}] {}".format(question.get("id"), question.get("question")))
        if question.get("reason"):
            print("Motivo: {}".format(question["reason"]))
        answer = ""
        while not answer.strip():
            answer = prompt("Respuesta (o :abort para detener y conservar el estado): ")
            if answer.strip() == ":abort":
                raise AbortedByUser("Ejecución detenida por el usuario durante las aclaraciones.")
            if not answer.strip():
                print("La respuesta no puede estar vacía.")
        responses.append({
            "phase": phase,
            "question_id": question.get("id"),
            "question": question.get("question"),
            "answer": answer,
            "answered_at": datetime.datetime.now().astimezone().isoformat(),
        })
        answers_path.write_text(
            json.dumps({"delivery_id": delivery_id, "responses": responses},
                       ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
