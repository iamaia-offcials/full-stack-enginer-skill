"""Keep translated installation instructions operationally consistent."""
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('ru', 'es', 'ar', 'tr', 'zh-CN')


class ReadmeTests(unittest.TestCase):
    def test_translations_preserve_executable_examples(self):
        english = (ROOT / 'README.md').read_text(encoding='utf-8')
        commands = re.findall(r'```bash\n(.*?)\n```', english, re.S)
        self.assertTrue(commands, 'The primary README must include installation examples')
        for language in LANGUAGES:
            with self.subTest(language=language):
                path = ROOT / 'docs/i18n' / f'README.{language}.md'
                translated = path.read_text(encoding='utf-8')
                self.assertEqual(re.findall(r'```bash\n(.*?)\n```', translated, re.S), commands)
                self.assertIn('(../../README.md)', translated)
                for other in LANGUAGES:
                    self.assertIn(f'(README.{other}.md)', translated)


if __name__ == '__main__':
    unittest.main()
