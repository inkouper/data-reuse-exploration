"""Download and validate a pinned official release without a Google account."""
import shutil
import subprocess
import tempfile
import zipfile
from pathlib import Path

from common import arguments, release_catalog, verify_file, write_json


def download(args):
    spec = release_catalog()[args.release]
    args.data_dir.mkdir(parents=True, exist_ok=True)
    archive = args.data_dir / spec['archive_name']
    csv_path = args.data_dir / spec['csv_member']
    if not archive.exists():
        with tempfile.NamedTemporaryFile(dir=args.data_dir, suffix='.part', delete=False) as f:
            temporary = Path(f.name)
        try:
            subprocess.run([
                'curl', '--fail', '--location', '--silent', '--show-error',
                '--proto', '=https', '--proto-redir', '=https', '--retry', '2',
                '--max-time', '300', '--max-filesize', str(spec['compressed_bytes']),
                '--output', str(temporary), '--url', spec['url'],
            ], check=True)
            verify_file(temporary, spec['compressed_bytes'], spec['archive_sha256'])
            temporary.replace(archive)
        finally:
            temporary.unlink(missing_ok=True)
        print(f'Downloaded {archive.name}', flush=True)
    else:
        verify_file(archive, spec['compressed_bytes'], spec['archive_sha256'])
        print(f'Reusing verified archive {archive.name}', flush=True)

    if csv_path.exists():
        verify_file(csv_path, spec['csv_bytes'], spec['csv_sha256'])
        print(f'Reusing verified CSV {csv_path.name}', flush=True)
    else:
        with tempfile.NamedTemporaryFile(dir=args.data_dir, suffix='.part', delete=False) as f:
            temporary = Path(f.name)
        try:
            # Select the exact member: __MACOSX contains an unrelated ._*.csv file.
            # Reading the complete member also verifies its ZIP CRC.
            with zipfile.ZipFile(archive) as zipped:
                info = zipped.getinfo(spec['csv_member'])
                if info.file_size != spec['csv_bytes']:
                    raise ValueError('Unexpected uncompressed release size')
                with zipped.open(info) as source, temporary.open('wb') as target:
                    shutil.copyfileobj(source, target)
            verify_file(temporary, spec['csv_bytes'], spec['csv_sha256'])
            temporary.replace(csv_path)
        finally:
            temporary.unlink(missing_ok=True)
        print(f'Extracted and CRC-checked {csv_path.name}', flush=True)

    manifest = {'release': args.release, **spec,
                'verification': 'Archive and CSV sizes and SHA-256 match the recorded local reference fingerprints. ZIP member CRC checked on extraction.'}
    write_json(args.output_dir / 'download-manifest.json', manifest)
    return manifest


if __name__ == '__main__':
    download(arguments(__doc__))
