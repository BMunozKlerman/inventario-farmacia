import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from sevencs.audit import AuditFailed, ClarificationGateClosed, audit  # noqa: E402

FIXTURES = Path(__file__).resolve().parent / "fixtures" / "one-postit"
DELIVERY = "BUDGET1"


class AuditTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.scratch = Path(self.temporary.name)
        self.com = self.scratch / "com"
        self.mapping = self.scratch / "mapping"
        self.clarifications = self.scratch / "clarifications"
        for directory in (self.com, self.mapping, self.clarifications):
            directory.mkdir()
        shutil.copy(FIXTURES / "com" / "BUDGET1-functional-front-p01.json", self.com)
        shutil.copy(FIXTURES / "mapping" / "BUDGET1-functional-front-traces.json", self.mapping)

    def audit(self, **overrides):
        options = dict(
            delivery_id=DELIVERY,
            com_directory=self.com,
            mapping_directory=self.mapping,
            clarification_directory=self.clarifications,
        )
        options.update(overrides)
        return audit(**options)

    def write_clarifications(self, questions):
        for phase in ("reading", "transformation"):
            path = self.clarifications / "{}-{}.json".format(DELIVERY, phase)
            payload = {"delivery_id": DELIVERY, "questions": questions}
            path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")

    def test_passes_when_every_sticky_has_a_trace(self):
        result = self.audit()
        self.assertTrue(result.passed)
        self.assertEqual(1, result.coverage)

    def test_fails_when_a_sticky_has_no_trace(self):
        (self.mapping / "BUDGET1-functional-front-traces.json").write_text(
            json.dumps({"traces": []}), encoding="utf-8"
        )
        result = self.audit()
        self.assertFalse(result.passed)
        self.assertEqual(0, result.coverage)

    def test_ignores_traces_that_point_to_an_unknown_sticky(self):
        (self.mapping / "BUDGET1-extra-traces.json").write_text(
            json.dumps({"traces": [{"sticky_id": "NO-EXISTE"}]}), encoding="utf-8"
        )
        self.assertEqual(1, self.audit().coverage)

    def test_falsifiability_check_rejects_a_run_that_would_otherwise_pass(self):
        self.assertFalse(self.audit(falsifiability_check=True).passed)

    def test_falsifiability_check_raises_when_there_is_nothing_to_reject(self):
        (self.com / "BUDGET1-functional-front-p01.json").write_text(
            json.dumps({"sections": [{"stickies": []}]}), encoding="utf-8"
        )
        with self.assertRaises(AuditFailed):
            self.audit(falsifiability_check=True)

    def test_raises_when_there_are_no_com_files(self):
        (self.com / "BUDGET1-functional-front-p01.json").unlink()
        with self.assertRaises(AuditFailed):
            self.audit()

    def test_clarification_gate_passes_when_every_question_is_closed(self):
        self.write_clarifications([])
        self.assertTrue(self.audit(require_clarification_gate=True).passed)

    def test_clarification_gate_rejects_an_open_question(self):
        self.write_clarifications([{"id": "Q-TEST-001", "question": "¿Cuál?", "status": "open"}])
        with self.assertRaises(ClarificationGateClosed):
            self.audit(require_clarification_gate=True)

    def test_clarification_gate_requires_both_phase_files(self):
        path = self.clarifications / "{}-reading.json".format(DELIVERY)
        path.write_text(json.dumps({"questions": []}), encoding="utf-8")
        with self.assertRaises(ClarificationGateClosed):
            self.audit(require_clarification_gate=True)

    def test_preserves_accents_when_reporting_an_open_question(self):
        question = "¿Qué simbologías de código de barras se aceptarán?"
        self.write_clarifications([{"id": "Q-TEST-001", "question": question, "status": "open"}])
        with self.assertRaises(ClarificationGateClosed) as raised:
            self.audit(require_clarification_gate=True)
        self.assertIn("1", str(raised.exception))


if __name__ == "__main__":
    unittest.main()
