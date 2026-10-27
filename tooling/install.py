#!/usr/bin/env python3
"""Install local Agent Skills. Python 3.10+, standard library; no network calls."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import stat
import sys
import tempfile
import uuid

SOURCE = Path(__file__).resolve().parents[1] / '.agents' / 'skills'
CORE = 'unified-development-standard'
MANIFEST = '.uds-install.json'
LOCATIONS = {
    'codex': ('.agents/skills', '.agents/skills'),
    'gemini': ('.gemini/skills', '.gemini/skills'),
    'claude': ('.claude/skills', '.claude/skills'),
    'antigravity': ('.agents/skills', '.gemini/config/skills'),
    'antigravity-cli': ('.agents/skills', '.gemini/antigravity-cli/skills'),
    'generic': ('.agents/skills', '.agents/skills'),
}

def reject_links(path: Path) -> None:
    """Refuse symlinks and Windows reparse points before traversal/mutation."""
    for item in [path, *path.parents]:
        try:
            info = item.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise ValueError(f'Linked/reparse path is not supported: {item}')

def files_hashes(folder: Path, include_manifest=False) -> dict[str, str]:
    reject_links(folder)
    result = {}
    for path in sorted(folder.rglob('*')):
        reject_links(path)
        if path.is_file() and (include_manifest or path != folder / MANIFEST):
            result[path.relative_to(folder).as_posix()] = hashlib.sha256(path.read_bytes()).hexdigest()
    return result

def skill_name(folder: Path) -> str:
    parts = (folder / 'SKILL.md').read_text(encoding='utf-8').split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError(f'Invalid manifest: {folder}')
    match = re.search(r'^name:\s*([a-z0-9-]+)\s*$', parts[1], re.M)
    if not match or match[1] != folder.name:
        raise ValueError(f'Nonmatching skill name: {folder}')
    return match[1]

def destination(args, home=None) -> Path:
    if args.target:
        if args.repo or args.scope == 'user':
            raise ValueError('Use --target alone, not together with --repo or --scope user')
        dest = args.target.expanduser().absolute()
    elif args.scope == 'user':
        if args.repo:
            raise ValueError('--repo is only valid with --scope repo')
        dest = (home or Path.home()) / LOCATIONS[args.agent][1]
    else:
        if not args.repo:
            raise ValueError('Specify --repo PATH for project installation, or --scope user')
        base = args.repo.expanduser().absolute()
        if not base.is_dir():
            raise ValueError(f'Project directory does not exist: {base}')
        dest = base / LOCATIONS[args.agent][0]
    reject_links(dest)
    dest = dest.resolve()
    source = SOURCE.resolve()
    if dest == source or source in dest.parents or dest in source.parents:
        raise ValueError('Source and destination must not overlap')
    return dest

def plan_install(dest, names, update, adopt):
    plan = []
    for name in names:
        source, target = SOURCE / name, dest / name
        skill_name(source)
        wanted = files_hashes(source)
        reject_links(target)
        action = 'ADD'
        expected = None
        if target.exists():
            if not target.is_dir():
                raise ValueError(f'Target is not a skill directory: {target}')
            skill_name(target)
            current = files_hashes(target)
            expected = files_hashes(target, include_manifest=True)
            marker = target / MANIFEST
            if marker.exists():
                saved = json.loads(marker.read_text(encoding='utf-8'))
                if not isinstance(saved, dict) or saved.get('installer') != 'uds' or saved.get('name') != name:
                    raise ValueError(f'Unrecognized installation manifest: {target}')
                if current != saved.get('files'):
                    raise ValueError(f'Local changes detected; preserve/merge them before updating: {target}')
            elif not (update and adopt):
                if current == wanted and not update:
                    print(f'UNCHANGED (unmanaged): {target}')
                    continue
                raise ValueError(f'Unmanaged skill: {target}. Review it, then use --update --adopt-existing to retain a backup.')
            if current == wanted and marker.exists():
                print(f'UNCHANGED: {target}')
                continue
            if not update:
                raise ValueError(f'Existing skill differs: {target}. Use --update after reviewing the source.')
            action = 'UPDATE'
        print(f'{action}: {target}')
        plan.append((source, target, wanted, expected))
    return plan

def apply_install(dest, plan):
    if not plan:
        return
    dest.mkdir(parents=True, exist_ok=True)
    backup_root = dest.parent / '.uds-backups' / uuid.uuid4().hex
    reject_links(backup_root)
    with tempfile.TemporaryDirectory(prefix='uds-stage-', dir=dest.parent) as staging:
        stage_root = Path(staging)
        for source, target, hashes, _ in plan:
            stage = stage_root / target.name
            shutil.copytree(source, stage)
            if files_hashes(stage) != hashes:
                raise ValueError(f'Source changed during installation: {source}')
            (stage / MANIFEST).write_text(json.dumps({
                'installer': 'uds', 'schema': 1, 'name': target.name, 'files': hashes,
            }, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
        completed = []
        try:
            for _, target, _, expected in plan:
                reject_links(target)
                actual = files_hashes(target, include_manifest=True) if target.exists() else None
                if actual != expected:
                    raise ValueError(f'Target changed during installation: {target}')
                backup = None
                if target.exists():
                    backup_root.mkdir(parents=True, exist_ok=True)
                    backup = backup_root / target.name
                    target.rename(backup)
                completed.append((target, backup))
                (stage_root / target.name).rename(target)
        except BaseException:
            for target, backup in reversed(completed):
                if target.exists():
                    target.rename(stage_root / (target.name + '-failed'))
                if backup is not None:
                    backup.rename(target)
            raise
    if backup_root.exists():
        print(f'Previous files retained in: {backup_root}')

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--agent', choices=LOCATIONS, default='codex')
    parser.add_argument('--scope', choices=['repo', 'user'], default='repo')
    parser.add_argument('--repo', type=Path, help='Existing project directory')
    parser.add_argument('--target', type=Path, help='Explicit skills directory for another compatible agent')
    parser.add_argument('--skills', default='core', help='core (default), all, or comma-separated skill names; core is always included')
    parser.add_argument('--list', action='store_true', help='List bundled skills without installing')
    parser.add_argument('--dry-run', action='store_true', help='Validate and show changes without writing')
    parser.add_argument('--update', action='store_true', help='Update unmodified managed skills, preserving backups')
    parser.add_argument('--adopt-existing', action='store_true', help='With --update, replace unmanaged matching-name skills, retaining backups')
    args = parser.parse_args(argv)
    lock = None
    try:
        available = {p.name for p in SOURCE.iterdir() if p.is_dir() and (p / 'SKILL.md').is_file()}
        if args.list:
            print('\n'.join(sorted(available)))
            return 0
        requested = {CORE} if args.skills == 'core' else available if args.skills == 'all' else set(args.skills.split(',')) | {CORE}
        if requested - available:
            raise ValueError('Unknown skills: ' + ', '.join(sorted(requested - available)))
        if args.adopt_existing and not args.update:
            raise ValueError('--adopt-existing requires --update')
        dest = destination(args)
        names = sorted(requested)
        if args.dry_run:
            plan = plan_install(dest, names, args.update, args.adopt_existing)
            print(f'DRY RUN: {len(plan)} changes; no files written.')
            return 0
        dest.parent.mkdir(parents=True, exist_ok=True)
        candidate = dest.parent / '.uds-install.lock'
        fd = os.open(candidate, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
        lock = candidate
        plan = plan_install(dest, names, args.update, args.adopt_existing)
        apply_install(dest, plan)
        print(f'Installed/updated {len(plan)} skills. Verify discovery in your agent: {dest}')
        return 0
    except (OSError, ValueError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 1
    finally:
        if lock is not None:
            lock.unlink()

if __name__ == '__main__':
    sys.exit(main())
