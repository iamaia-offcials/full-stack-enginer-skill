#!/usr/bin/env python3
"""Validate this package's small frontmatter subset, links and rule IDs; no runtime claims."""
from __future__ import annotations
import argparse
import csv
import json
from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
RULE = re.compile(r'\[([A-Z][A-Z0-9]+-\d{3})\]\s+(MUST|SHOULD|MAY)\b')
LINK = re.compile(r'\[[^\]]*\]\(([^)]+)\)')
SKIP = {'.git', '__pycache__', '.venv', 'dist', 'node_modules'}

def metadata(text):
    if not text.startswith('---\n'):
        raise ValueError('missing YAML frontmatter')
    parts = text.split('---', 2)
    if len(parts) != 3:
        raise ValueError('unclosed YAML frontmatter')
    fields = {}
    for line in parts[1].strip().splitlines():
        key, sep, value = line.partition(':')
        if not sep or key not in {'name', 'description'} or key in fields:
            raise ValueError('expected one name and description field (supported package subset)')
        value = value.strip()
        if value.startswith('"'):
            value = json.loads(value)
        elif ': ' in value or ' #' in value or value[:1] in "'[{&*!>|%@`":
            raise ValueError('quote frontmatter strings with JSON-compatible double quotes')
        if not isinstance(value, str) or not value:
            raise ValueError('empty/non-string metadata')
        fields[key] = value
    if set(fields) != {'name', 'description'}:
        raise ValueError('name and description are required')
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', fields['name']) or len(fields['name']) > 64:
        raise ValueError('invalid skill name')
    if len(fields['description']) > 1024:
        raise ValueError('description exceeds 1024 characters')
    return fields

def validate(root=ROOT):
    root = root.resolve()
    errors = []
    skills = root / '.agents/skills'
    folders = sorted(p for p in skills.iterdir() if p.is_dir()) if skills.exists() else []
    if not folders:
        errors.append('No skills found')
    names = set()
    core_license = skills / 'unified-development-standard/LICENSE'
    if (root / 'LICENSE').is_file() and (skills / 'unified-development-standard').is_dir():
        if not core_license.is_file() or core_license.read_bytes() != (root / 'LICENSE').read_bytes():
            errors.append('Bundled core LICENSE must match the repository LICENSE')
    for folder in folders:
        f = folder / 'SKILL.md'
        try:
            body = f.read_text(encoding='utf-8')
            meta = metadata(body)
            if meta['name'] != folder.name:
                errors.append(f'{f.relative_to(root)}: directory/name mismatch')
            names.add(meta['name'])
            if len(body.splitlines()) > 500:
                errors.append(f'{f.relative_to(root)}: entrypoint exceeds 500 lines')
            if any(p != f for p in folder.rglob('SKILL.md')):
                errors.append(f'{folder.name}: nested skill manifests')
        except (OSError, ValueError) as exc:
            errors.append(f'{f.relative_to(root)}: {exc}')
    ids = {}
    for f in sorted(root.rglob('*.md')):
        if any(part in SKIP for part in f.relative_to(root).parts):
            continue
        text = f.read_text(encoding='utf-8')
        rel = f.relative_to(root)
        if 'references' in rel.parts:
            for match in RULE.finditer(text):
                rule_id = match[1]
                if rule_id in ids:
                    errors.append(f'Duplicate {rule_id}: {ids[rule_id]} and {rel}')
                ids[rule_id] = rel
        # Fenced code contains illustrative paths, not live documentation links.
        text = re.sub(r'(?ms)^```.*?^```[^\n]*$', '', text)
        for match in LINK.finditer(text):
            target = match[1].strip()
            if target.startswith('<'):
                target = target.split('>', 1)[0][1:]
            else:
                target = target.split(' ', 1)[0]
            parsed = urlsplit(target)
            if parsed.scheme or not parsed.path:
                continue
            dest = (f.parent / unquote(parsed.path)).resolve()
            if root not in dest.parents and dest != root:
                errors.append(f'{rel}: link escapes package: {target}')
            elif not dest.exists():
                errors.append(f'{rel}: broken link: {target}')
    matrix = root / 'tooling/ROUTING_TESTS.csv'
    if matrix.exists():
        with matrix.open(encoding='utf-8', newline='') as f:
            for row in csv.DictReader(f):
                for key in ('expected_primary', 'should_not_activate'):
                    if row[key] != 'none' and row[key] not in names:
                        errors.append(f'Routing matrix: unknown skill {row[key]}')
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    args = parser.parse_args()
    errors = validate(args.root)
    for error in errors:
        print('ERROR:', error)
    print(f'{"FAIL" if errors else "PASS"}: package metadata, Markdown links and unique rule IDs ({len(errors)} errors).')
    print('Does not certify engineering correctness, live agent discovery, security or deployment.')
    return int(bool(errors))

if __name__ == '__main__':
    sys.exit(main())
