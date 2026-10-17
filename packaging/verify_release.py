#!/usr/bin/env python3
"""Assemble the exact, checksum-verified installers from the public update feed."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil


def prepare(root, output):
    manifest = json.loads((root / 'releases/latest.json').read_text())
    version = manifest['version']
    if not re.fullmatch(r'\d+\.\d+\.\d+', version):
        raise ValueError('Invalid release version')
    if (root / 'VERSION').read_text().strip() != version:
        raise ValueError('Source version and update feed disagree')
    release_dir = root / 'releases' / version
    output.mkdir(parents=True, exist_ok=True)

    def source(path):
        candidate = (root / path).resolve()
        if not candidate.is_relative_to(release_dir.resolve()) or not candidate.is_file():
            raise ValueError('Asset path is outside its release directory')
        return candidate

    for platform in ('android', 'linux'):
        asset = manifest['assets'][platform]
        target = output / Path(asset['path']).name
        with target.open('wb') as stream:
            if asset.get('parts'):
                for part in asset['parts']:
                    data = source(part['path']).read_bytes()
                    if len(data) != part['size'] or hashlib.sha256(data).hexdigest() != part['sha256']:
                        raise ValueError('Installer part failed verification')
                    stream.write(data)
            else:
                stream.write(source(asset['path']).read_bytes())
        data = target.read_bytes()
        if len(data) != asset['size'] or hashlib.sha256(data).hexdigest() != asset['sha256']:
            raise ValueError('Assembled installer failed verification')
    for name in ('L4NTrak_Feature_and_Test_Report.md', 'L4NTrak_Quick_Start.md'):
        shutil.copyfile(release_dir / name, output / name)
    shutil.copyfile(root / 'releases/latest.json', output / f'L4NTrak_{version}_Update_Manifest.json')
    assets = sorted(output.iterdir())
    (output / 'SHA256SUMS.txt').write_text(''.join(
        f'{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n' for path in assets
        if path.is_file() and path.name not in ('SHA256SUMS.txt', 'release-notes.md')
    ))
    (output / 'release-notes.md').write_text(
        f'L4NTrak {version} for Android and Linux Mint/Debian. Install over the existing app to retain its data.\n\n'
        + manifest['notes'] + '\n\n'
        + 'Includes the APK, DEB, update manifest, SHA-256 checksums, quick start and feature/test report. '
        + 'Source and downloads retain this repository\'s public visibility. '
        + 'Physical GPS, phone radio, microphone/voice quality and local AI inference still require device checks.\n'
    )
    return version


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    print(prepare(args.root.resolve(), args.output_dir.resolve()))
