#!/usr/bin/env python3
"""Presupuesto de un post-it: cobertura, rechazo por falsabilidad y compuerta de aclaraciones."""

import json
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from sevencs.audit import ClarificationGateClosed, audit  # noqa: E402
from validate_skills import validate  # noqa: E402

FIXTURES = ROOT / "tests" / "fixtures" / "one-postit"
SCRATCH = ROOT / "tmp" / "one-postit-budget"
DELIVERY = "BUDGET1"
EXPECTED_QUESTION = "¿Qué simbologías de código de barras se aceptarán?"


class OnePostitBudgetTest(unittest.TestCase):
    def setUp(self):
        if SCRATCH.exists():
            shutil.rmtree(SCRATCH)
        for name in ("com", "mapping", "clarifications"):
            (SCRATCH / name).mkdir(parents=True)
        shutil.copy(FIXTURES / "com" / "BUDGET1-functional-front-p01.json", SCRATCH / "com")
        shutil.copy(
            FIXTURES / "mapping" / "BUDGET1-functional-front-traces.json", SCRATCH / "mapping"
        )

    def audit(self, **overrides):
        options = dict(
            delivery_id=DELIVERY,
            com_directory=SCRATCH / "com",
            mapping_directory=SCRATCH / "mapping",
            clarification_directory=SCRATCH / "clarifications",
        )
        options.update(overrides)
        return audit(**options)

    def write_clarifications(self, questions):
        for phase in ("reading", "transformation"):
            path = SCRATCH / "clarifications" / "{}-{}.json".format(DELIVERY, phase)
            path.write_text(
                json.dumps({"delivery_id": DELIVERY, "questions": questions}, ensure_ascii=False),
                encoding="utf-8",
            )

    def test_every_skill_declares_valid_frontmatter(self):
        self.assertEqual(12, validate(ROOT))

    def test_a_single_traced_postit_reaches_full_coverage(self):
        self.assertEqual(1, self.audit().coverage)

    def test_the_auditor_rejects_an_artificially_missing_trace(self):
        self.assertFalse(self.audit(falsifiability_check=True).passed)

    def test_the_gate_lets_the_audit_run_when_no_question_is_open(self):
        self.write_clarifications([])
        self.assertTrue(self.audit(require_clarification_gate=True).passed)

    def test_the_gate_blocks_the_audit_when_a_question_is_open(self):
        self.write_clarifications(
            [{"id": "Q-TEST-001", "question": EXPECTED_QUESTION, "status": "open"}]
        )
        with self.assertRaises(ClarificationGateClosed):
            self.audit(require_clarification_gate=True)

    def test_clarifications_survive_a_utf8_round_trip(self):
        self.write_clarifications(
            [{"id": "Q-TEST-001", "question": EXPECTED_QUESTION, "status": "open"}]
        )
        path = SCRATCH / "clarifications" / "{}-transformation.json".format(DELIVERY)
        with open(path, encoding="utf-8") as handle:
            decoded = json.load(handle)["questions"][0]["question"]
        self.assertEqual(EXPECTED_QUESTION, decoded)


if __name__ == "__main__":
    unittest.main()
