"""End-to-end installer checks; all mutations stay in temporary directories."""
import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
import os
from unittest.mock import patch
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "tooling" / "install.py"
CORE = "unified-development-standard"
spec = importlib.util.spec_from_file_location("installer", SCRIPT)
installer = importlib.util.module_from_spec(spec)
spec.loader.exec_module(installer)


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix="uds-test-")
        self.base = Path(self.temp.name)
        self.repo = self.base / "project with spaces"
        self.repo.mkdir()

    def tearDown(self):
        self.temp.cleanup()

    def run_cli(self, *args, ok=True):
        result = subprocess.run(
            [sys.executable, str(SCRIPT), *map(str, args)],
            capture_output=True, text=True, encoding="utf-8", cwd=self.base,
        )
        if ok:
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        else:
            self.assertNotEqual(result.returncode, 0, result.stdout + result.stderr)
        return result

    def install(self, *args, ok=True):
        return self.run_cli("--scope", "repo", "--repo", self.repo, *args, ok=ok)

    def test_default_is_self_contained_core(self):
        self.install()
        skills = self.repo / ".agents/skills"
        self.assertEqual([p.name for p in skills.iterdir()], [CORE])
        self.assertTrue((skills / CORE / "guides/LIVING-DOCUMENTATION.md").is_file())

    def test_native_project_destinations(self):
        for agent, folder in [("codex", ".agents"), ("gemini", ".gemini"),
                              ("claude", ".claude"), ("antigravity", ".agents"),
                              ("antigravity-cli", ".agents")]:
            with self.subTest(agent=agent):
                repo = self.base / agent
                repo.mkdir()
                self.run_cli("--agent", agent, "--repo", repo)
                self.assertTrue((repo / folder / "skills" / CORE / "SKILL.md").is_file())

    def test_dry_run_writes_nothing(self):
        before = list(self.repo.rglob("*"))
        self.install("--dry-run")
        self.assertEqual(list(self.repo.rglob("*")), before)

    def test_specialization_includes_core(self):
        self.install("--skills", "uds-security")
        names = {p.name for p in (self.repo / ".agents/skills").iterdir()}
        self.assertEqual(names, {CORE, "uds-security"})

    def test_unknown_skill_leaves_no_partial_install(self):
        self.install("--skills", "uds-security,../../escape", ok=False)
        self.assertEqual(list(self.repo.iterdir()), [])

    def test_repeat_install_is_noop(self):
        self.install()
        f = self.repo / ".agents/skills" / CORE / "SKILL.md"
        previous = f.stat().st_mtime_ns
        self.install()
        self.assertEqual(f.stat().st_mtime_ns, previous)

    def test_never_overwrites_unmanaged_skill_implicitly(self):
        folder = self.repo / ".agents/skills" / CORE
        folder.mkdir(parents=True)
        f = folder / "SKILL.md"
        f.write_text(f"---\nname: {CORE}\ndescription: Local customization\n---\nMine", encoding="utf-8")
        self.install("--update", ok=False)
        self.assertIn("Mine", f.read_text(encoding="utf-8"))

    def test_explicit_adoption_keeps_backup(self):
        folder = self.repo / ".agents/skills" / CORE
        folder.mkdir(parents=True)
        f = folder / "SKILL.md"
        original = f"---\nname: {CORE}\ndescription: Legacy\n---\nLocal content"
        f.write_text(original, encoding="utf-8")
        self.install("--update", "--adopt-existing")
        backups = list((self.repo / ".agents/.uds-backups").rglob("SKILL.md"))
        self.assertTrue(any(p.read_text(encoding="utf-8") == original for p in backups))
        self.assertNotEqual(f.read_text(encoding="utf-8"), original)

    def test_modified_managed_file_is_preserved(self):
        self.install()
        f = self.repo / ".agents/skills" / CORE / "SKILL.md"
        f.write_text(f.read_text(encoding="utf-8") + "\nUser edit", encoding="utf-8")
        self.install("--update", ok=False)
        self.assertTrue(f.read_text(encoding="utf-8").endswith("User edit"))

    def test_added_user_file_is_preserved(self):
        self.install()
        f = self.repo / ".agents/skills" / CORE / "notes.txt"
        f.write_text("mine", encoding="utf-8")
        self.install("--update", ok=False)
        self.assertEqual(f.read_text(encoding="utf-8"), "mine")

    def test_custom_target_and_instruction_files_untouched(self):
        for name in ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]:
            (self.repo / name).write_text("Existing rules", encoding="utf-8")
        target = self.repo / "custom skills"
        self.run_cli("--target", target)
        self.assertTrue((target / CORE / "SKILL.md").is_file())
        for name in ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]:
            self.assertEqual((self.repo / name).read_text(encoding="utf-8"), "Existing rules")

    def test_refuse_source_destination_overlap(self):
        self.run_cli("--target", ROOT / ".agents/skills", ok=False)

    def test_symlink_destination_refused(self):
        outside = self.base / "outside"
        outside.mkdir()
        link = self.repo / ".agents"
        try:
            link.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest("Symlink creation unavailable on this host")
        self.install(ok=False)
        self.assertEqual(list(outside.iterdir()), [])

    def test_all_skills(self):
        self.install("--skills", "all")
        names = {p.name for p in (self.repo / ".agents/skills").iterdir()}
        source = {p.name for p in (ROOT / ".agents/skills").iterdir() if (p / "SKILL.md").is_file()}
        self.assertEqual(names, source)

    def test_nested_manifest_name_is_not_ignored(self):
        self.install()
        f = self.repo / ".agents/skills" / CORE / "references/.uds-install.json"
        f.write_text("user data", encoding="utf-8")
        self.install("--update", ok=False)
        self.assertEqual(f.read_text(encoding="utf-8"), "user data")

    def test_edit_between_plan_and_apply_aborts(self):
        dest = self.repo / ".agents/skills"
        folder = dest / CORE
        folder.mkdir(parents=True)
        f = folder / "SKILL.md"
        f.write_text(f"---\nname: {CORE}\ndescription: Legacy\n---\nOld", encoding="utf-8")
        plan = installer.plan_install(dest, [CORE], True, True)
        f.write_text(f.read_text(encoding="utf-8") + "\nNew user edit", encoding="utf-8")
        with self.assertRaises(ValueError):
            installer.apply_install(dest, plan)
        self.assertTrue(f.read_text(encoding="utf-8").endswith("New user edit"))

    def test_swap_failure_restores_previous_install(self):
        dest = self.repo / ".agents/skills"
        folder = dest / CORE
        folder.mkdir(parents=True)
        f = folder / "SKILL.md"
        old = f"---\nname: {CORE}\ndescription: Legacy\n---\nOld"
        f.write_text(old, encoding="utf-8")
        plan = installer.plan_install(dest, [CORE], True, True)
        rename = Path.rename
        def fail_new_swap(path, target):
            if path.parent.name.startswith("uds-stage-") and path.name == CORE:
                raise OSError("simulated swap failure")
            return rename(path, target)
        with patch.object(Path, "rename", fail_new_swap):
            with self.assertRaises(OSError):
                installer.apply_install(dest, plan)
        self.assertEqual(f.read_text(encoding="utf-8"), old)

    def test_global_agent_paths(self):
        import argparse
        expected = {"codex": ".agents/skills", "gemini": ".gemini/skills",
                    "claude": ".claude/skills", "antigravity": ".gemini/config/skills",
                    "antigravity-cli": ".gemini/antigravity-cli/skills"}
        for agent, rel in expected.items():
            args = argparse.Namespace(agent=agent, scope="user", repo=None, target=None)
            self.assertEqual(installer.destination(args, self.base), self.base / rel)

    def test_managed_upgrade_keeps_previous_version(self):
        source = self.base / "source"
        folder = source / CORE
        folder.mkdir(parents=True)
        old = f'---\nname: {CORE}\ndescription: Initial\n---\nOld behavior'
        new = old.replace('Old behavior', 'New behavior')
        (folder / 'SKILL.md').write_text(old, encoding='utf-8')
        dest = self.repo / '.agents/skills'
        with patch.object(installer, 'SOURCE', source):
            installer.apply_install(dest, installer.plan_install(dest, [CORE], False, False))
            (folder / 'SKILL.md').write_text(new, encoding='utf-8')
            installer.apply_install(dest, installer.plan_install(dest, [CORE], True, False))
        self.assertEqual((dest / CORE / 'SKILL.md').read_text(encoding='utf-8'), new)
        backups = list((dest.parent / '.uds-backups').rglob('SKILL.md'))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding='utf-8'), old)

    @unittest.skipUnless(os.name == 'nt', 'Windows junction behavior')
    def test_windows_junction_is_refused(self):
        outside = self.base / 'outside'
        outside.mkdir()
        link = self.repo / '.agents'
        quote = lambda p: "'" + str(p).replace("'", "''") + "'"
        cmd = f"New-Item -ItemType Junction -Path {quote(link)} -Target {quote(outside)} -ErrorAction Stop | Out-Null"
        creation = subprocess.run(['powershell', '-NoProfile', '-Command', cmd], capture_output=True, text=True)
        self.assertEqual(creation.returncode, 0, creation.stderr)
        self.install(ok=False)
        self.assertEqual(list(outside.iterdir()), [])


if __name__ == "__main__":
    unittest.main()
