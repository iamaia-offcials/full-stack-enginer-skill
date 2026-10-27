import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("validator", ROOT / "tooling/validate_suite.py")
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="uds-validation-")
        self.root = Path(self.tmp.name)
        self.skill = self.root / ".agents/skills/example"
        self.skill.mkdir(parents=True)
        (self.skill / "SKILL.md").write_text('---\nname: example\ndescription: "Use for examples"\n---\n# Example\n', encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def test_valid_minimal_skill(self):
        self.assertEqual(validator.validate(self.root), [])

    def test_links_in_guides_are_checked(self):
        (self.skill / "guides").mkdir()
        (self.skill / "guides/test.md").write_text("[missing](no-such-file.md)", encoding="utf-8")
        self.assertTrue(any("no-such-file.md" in e for e in validator.validate(self.root)))

    def test_root_readme_is_checked(self):
        (self.root / "README.md").write_text("[missing](deleted-guide.md)", encoding="utf-8")
        self.assertTrue(any("deleted-guide.md" in e for e in validator.validate(self.root)))

    def test_bad_frontmatter_is_rejected(self):
        (self.skill / "SKILL.md").write_text('---\nname: example\ndescription: Unquoted: unsafe YAML\n---\n', encoding="utf-8")
        self.assertTrue(validator.validate(self.root))

    def test_duplicate_rule_id_is_rejected(self):
        (self.skill / "references").mkdir()
        (self.skill / "references/a.md").write_text('- `[ABC-001] MUST` a\n- `[ABC-001] MUST` b', encoding="utf-8")
        self.assertTrue(any("ABC-001" in e for e in validator.validate(self.root)))


if __name__ == "__main__":
    unittest.main()
