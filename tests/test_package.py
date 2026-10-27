import hashlib
import subprocess
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class PackageTests(unittest.TestCase):
    def test_archive_is_portable_and_reproducible(self):
        with tempfile.TemporaryDirectory(prefix="uds-package-") as directory:
            output = Path(directory) / "skill.zip"
            def build():
                run = subprocess.run([sys.executable, str(ROOT / "tooling/package.py"),
                                      "--output", str(output)], capture_output=True, text=True)
                self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
                return hashlib.sha256(output.read_bytes()).hexdigest()
            first = build()
            self.assertEqual(first, build())
            with zipfile.ZipFile(output) as z:
                self.assertIsNone(z.testzip())
                names = z.namelist()
                self.assertEqual(sum(n.endswith("/SKILL.md") for n in names), 1)
                self.assertIn("unified-development-standard/LICENSE", names)
                self.assertIn("unified-development-standard/guides/LIVING-DOCUMENTATION.md", names)
                self.assertFalse(any("legacy" in n or "__pycache__" in n for n in names))
                self.assertFalse(any("/README" in n or "/i18n/" in n for n in names),
                                 "Human README translations must stay outside the skill payload")
                self.assertLess(len(names), 200)
                self.assertTrue(all(i.file_size < 1024 * 1024 for i in z.infolist()))


if __name__ == "__main__":
    unittest.main()
