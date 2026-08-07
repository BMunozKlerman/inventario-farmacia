import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

from sevencs.paths import PathOutsideRepo, repo_path, resolve_pdf  # noqa: E402


class RepoPathTest(unittest.TestCase):
    def test_resolves_a_relative_path_against_the_repository_root(self):
        root = Path("/repo")
        self.assertEqual(Path("/repo/com/E1.json"), repo_path(root, "com/E1.json"))

    def test_accepts_native_separators(self):
        root = Path("/repo")
        self.assertEqual(repo_path(root, "com/E1.json"), repo_path(root, Path("com") / "E1.json"))

    def test_keeps_an_absolute_path_untouched(self):
        self.assertEqual(Path("/otro/E1.json"), repo_path(Path("/repo"), "/otro/E1.json"))


class ResolvePdfTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        (self.root / "resources").mkdir()
        self.pdf = self.root / "resources" / "canvas.pdf"
        self.pdf.write_bytes(b"%PDF-1.4")

    def test_returns_the_absolute_path_of_a_pdf_inside_resources(self):
        self.assertEqual(self.pdf, resolve_pdf(self.root, "resources/canvas.pdf"))

    def test_rejects_a_pdf_outside_resources(self):
        outside = self.root / "fuera.pdf"
        outside.write_bytes(b"%PDF-1.4")
        with self.assertRaises(PathOutsideRepo):
            resolve_pdf(self.root, outside)

    def test_rejects_a_traversal_that_escapes_resources(self):
        with self.assertRaises(PathOutsideRepo):
            resolve_pdf(self.root, "resources/../fuera.pdf")

    def test_rejects_a_missing_file(self):
        with self.assertRaises(FileNotFoundError):
            resolve_pdf(self.root, "resources/ausente.pdf")


if __name__ == "__main__":
    unittest.main()
