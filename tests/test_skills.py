import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from sevencs.skills import SkillNotFound, inline_skills, load_skill  # noqa: E402

SKILLS_ROOT = ROOT / ".agents" / "skills"


class LoadSkillTest(unittest.TestCase):
    def test_includes_the_body_of_the_skill(self):
        text = load_skill(SKILLS_ROOT, "7cs-spec-audit")
        self.assertIn("post-its con traza válida", text)

    def test_strips_the_yaml_frontmatter(self):
        text = load_skill(SKILLS_ROOT, "7cs-spec-audit")
        self.assertNotIn("description:", text)
        self.assertFalse(text.lstrip().startswith("---"))

    def test_appends_every_reference_document(self):
        text = load_skill(SKILLS_ROOT, "7cs-canvas-ingest")
        self.assertIn("pipeline-contract.md", text)

    def test_a_skill_without_references_loads_cleanly(self):
        self.assertIn("7cs-structural", load_skill(SKILLS_ROOT, "7cs-structural"))

    def test_raises_for_an_unknown_skill(self):
        with self.assertRaises(SkillNotFound):
            load_skill(SKILLS_ROOT, "7cs-inexistente")


class InlineSkillsTest(unittest.TestCase):
    def test_concatenates_every_requested_skill(self):
        block = inline_skills(SKILLS_ROOT, ["7cs-structural", "7cs-deployment"])
        self.assertIn("7cs-structural", block)
        self.assertIn("7cs-deployment", block)

    def test_tells_the_agent_not_to_look_for_skill_files(self):
        block = inline_skills(SKILLS_ROOT, ["7cs-structural"])
        self.assertIn("no busques", block.lower())

    def test_separates_skills_so_their_contents_do_not_blend(self):
        block = inline_skills(SKILLS_ROOT, ["7cs-structural", "7cs-deployment"])
        self.assertEqual(2, block.count("===== SKILL:"))

    def test_every_skill_used_by_the_pipeline_can_be_inlined(self):
        from run_pipeline import BACKEND_SKILLS, COMPOSE_SKILLS, READING_SKILLS, TRANSFORM_SKILLS

        for names in (READING_SKILLS, TRANSFORM_SKILLS, COMPOSE_SKILLS, BACKEND_SKILLS):
            self.assertTrue(inline_skills(SKILLS_ROOT, names).strip())


if __name__ == "__main__":
    unittest.main()
