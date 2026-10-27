#!/usr/bin/env python3
"""Read selected reference records, or rebuild/check the derived offline gallery. No network."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

CORE = Path(__file__).resolve().parents[1]
FILES = {'ux': 'assets/ux/cases.json', 'scenario': 'assets/ux/scenarios.json',
         'motion': 'assets/motion/patterns.json'}
GALLERY = CORE / 'examples/reference-atlas.html'


def records(kind):
    return json.loads((CORE / FILES[kind]).read_text(encoding='utf-8'))


def gallery_text():
    template = (CORE / 'assets/atlas-template.html').read_text(encoding='utf-8')
    if template.count('@@ATLAS_DATA@@') != 1:
        raise ValueError('Expected exactly one gallery data placeholder')
    data = json.dumps({kind: records(kind) for kind in FILES}, ensure_ascii=False,
                      separators=(',', ':')).replace('<', '\\u003c')
    return template.replace('@@ATLAS_DATA@@', data)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--kind', choices=FILES, default='ux')
    parser.add_argument('--id', help='Exact reference ID; returns only that full record')
    parser.add_argument('--niche', help='Exact sector from the reference metadata')
    parser.add_argument('--model', choices=['catalog', 'information', 'hybrid'])
    parser.add_argument('--query', default='', help='Case-insensitive search')
    parser.add_argument('--limit', type=int, default=3, help='Summary limit, 1–10 (default: 3)')
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--build-gallery', action='store_true')
    mode.add_argument('--check-gallery', action='store_true')
    args = parser.parse_args()
    try:
        if args.build_gallery or args.check_gallery:
            expected = gallery_text()
            if args.check_gallery:
                if not GALLERY.is_file() or GALLERY.read_text(encoding='utf-8') != expected:
                    raise ValueError('Gallery is missing/stale; run --build-gallery')
                print('PASS: gallery matches canonical reference data and template')
            else:
                if GALLERY.is_symlink() or GALLERY.parent.is_symlink():
                    raise ValueError('Refusing linked gallery output')
                GALLERY.parent.mkdir(parents=True, exist_ok=True)
                GALLERY.write_text(expected, encoding='utf-8', newline='\n')
                print(GALLERY)
            return 0
        if not 1 <= args.limit <= 10:
            parser.error('--limit must be between 1 and 10')
        selected = records(args.kind)
        if args.id:
            found = next((r for r in selected if r['id'] == args.id), None)
            if found is None:
                parser.error('Unknown reference ID for this kind')
            print(json.dumps(found, ensure_ascii=False, indent=2))
            return 0
        selected = [r for r in selected
                    if (not args.niche or r.get('niche') == args.niche)
                    and (not args.model or r.get('model') == args.model)
                    and args.query.casefold() in json.dumps(r, ensure_ascii=False).casefold()]
        keys = ('id', 'name', 'title', 'niche', 'model', 'category', 'evidence', 'visual_status')
        summaries = [{k: r[k] for k in keys if k in r} for r in selected[:args.limit]]
        print(json.dumps({'matches': summaries, 'total_matching': len(selected),
                          'next': 'Read a selected full record with --kind and --id'},
                         ensure_ascii=False, indent=2))
        return 0
    except (OSError, ValueError) as exc:
        parser.exit(1, f'ERROR: {exc}\n')


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    sys.exit(main())
