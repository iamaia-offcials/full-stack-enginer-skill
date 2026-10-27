#!/usr/bin/env python3
"""Build one self-contained Agent Skills ZIP from the current validated sources."""
from __future__ import annotations
import argparse
import os
from pathlib import Path
import tempfile
import zipfile

from install import CORE, SOURCE, reject_links
from validate_suite import ROOT, validate


def build(output: Path) -> None:
    errors = validate(ROOT)
    if errors:
        raise ValueError("Package validation failed:\n" + "\n".join(errors))
    reject_links(output.absolute())
    output = output.resolve()
    if output.suffix != '.zip' or SOURCE.resolve() in output.parents:
        raise ValueError('Choose a .zip output outside the skill source directory')
    folder = SOURCE / CORE
    payload = []
    for path in sorted(folder.rglob('*')):
        reject_links(path)
        if path.is_file():
            payload.append((CORE + '/' + path.relative_to(folder).as_posix(), path.read_bytes()))
    output.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(suffix='.zip', dir=output.parent)
    os.close(fd)
    temporary = Path(name)
    try:
        with zipfile.ZipFile(temporary, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
            for name, data in payload:
                info = zipfile.ZipInfo(name, date_time=(1980, 1, 1, 0, 0, 0))
                info.compress_type = zipfile.ZIP_DEFLATED
                info.create_system = 3
                info.external_attr = 0o100644 << 16
                archive.writestr(info, data)
        with zipfile.ZipFile(temporary) as archive:
            if archive.testzip() is not None:
                raise ValueError('Archive integrity check failed')
        temporary.replace(output)
    finally:
        temporary.unlink(missing_ok=True)
    print(f'{output} ({len(payload)} files)')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path, default=ROOT / 'dist' / (CORE + '.zip'))
    args = parser.parse_args()
    try:
        build(args.output)
    except (ValueError, OSError) as exc:
        parser.exit(1, f'ERROR: {exc}\n')


if __name__ == '__main__':
    main()
