"""Reference preservation, selective reading and portable gallery checks."""
import hashlib
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
CORE = ROOT / '.agents/skills/unified-development-standard'
SCRIPT = CORE / 'scripts/reference_atlas.py'


class ReferenceAtlasTests(unittest.TestCase):
    def test_original_case_coverage_and_evidence_remain_explicit(self):
        cases = json.loads((CORE / 'assets/ux/cases.json').read_text(encoding='utf-8'))
        self.assertEqual({c['id'] for c in cases}, {f'RW-{n:03}' for n in range(1, 40)})
        self.assertEqual(sum(c['evidence'] == 'secondary' for c in cases), 3)
        self.assertEqual(len({c['niche'] for c in cases}), 6)
        for c in cases:
            self.assertEqual(c['visual_status'], 'not-captured')
            self.assertEqual(c['verification_status'], 'supplied-observation-not-revalidated')
            self.assertTrue(c['url'].startswith('https://'))
            self.assertTrue(c['principle'].startswith('Hypothesis: '))
            if c['evidence'] == 'secondary':
                self.assertTrue(c['secondary'].startswith('https://'))
        scenarios = json.loads((CORE / 'assets/ux/scenarios.json').read_text(encoding='utf-8'))
        self.assertEqual({s['id'] for s in scenarios}, {f'UX-S{n:02}' for n in range(1, 13)})
        self.assertTrue(all(s['alternative_a'] and s['alternative_b'] for s in scenarios))

    def test_all_motion_visuals_are_present_and_intact(self):
        folder = CORE / 'assets/motion'
        patterns = json.loads((folder / 'patterns.json').read_text(encoding='utf-8'))
        self.assertEqual(len({p['id'] for p in patterns}), 27)
        for p in patterns:
            for field, signature in [('storyboard', b'\x89PNG'), ('animation', b'GIF8')]:
                asset = (folder / p[field]).resolve()
                self.assertIn(folder.resolve(), asset.parents)
                self.assertTrue(asset.read_bytes().startswith(signature))
                self.assertEqual(hashlib.sha256(asset.read_bytes()).hexdigest(), p[field + '_sha256'])

    def run_selector(self, *args):
        return subprocess.run([sys.executable, str(SCRIPT), *args], capture_output=True,
                              text=True, encoding='utf-8')

    def test_default_selection_is_bounded_and_case_lookup_is_exact(self):
        run = self.run_selector('--kind', 'ux', '--niche', 'tourism', '--limit', '2')
        self.assertEqual(run.returncode, 0, run.stderr)
        result = json.loads(run.stdout)
        self.assertEqual(len(result['matches']), 2)
        self.assertTrue(all(c['niche'] == 'tourism' for c in result['matches']))
        self.assertNotIn('observed', result['matches'][0])
        case = self.run_selector('--kind', 'ux', '--id', 'RW-020')
        self.assertEqual(case.returncode, 0, case.stderr)
        self.assertEqual(json.loads(case.stdout)['id'], 'RW-020')
        self.assertNotEqual(self.run_selector('--kind', 'ux', '--id', '../../secret').returncode, 0)

    def test_gallery_matches_canonical_data_without_rewriting(self):
        run = self.run_selector('--check-gallery')
        self.assertEqual(run.returncode, 0, run.stderr + run.stdout)


if __name__ == '__main__':
    unittest.main()
