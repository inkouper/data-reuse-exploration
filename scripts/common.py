"""Shared paths and provenance for the published exploration scripts."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
COLUMNS = ['publication_doi', 'dataset_id', 'dataset_id_type', 'repository',
           'citation_type', 'release']


def release_catalog():
    return json.loads((ROOT / 'references' / 'releases.json').read_text())


def arguments(description):
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('--release', choices=release_catalog(), default='202610')
    parser.add_argument('--data-dir', type=Path,
                        help='Local data/database directory; default: <repo>/data/<release>')
    parser.add_argument('--output-dir', type=Path,
                        help='Summary directory; default: <repo>/results/<release>')
    args = parser.parse_args()
    args.data_dir = (args.data_dir or ROOT / 'data' / args.release).resolve()
    args.output_dir = (args.output_dir or ROOT / 'results' / args.release).resolve()
    return args


def sha256(path):
    with path.open('rb') as stream:
        return hashlib.file_digest(stream, 'sha256').hexdigest()


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def query(connection, sql, parameters=None):
    cursor = connection.execute(sql, parameters or [])
    return [dict(zip([d[0] for d in cursor.description], row)) for row in cursor.fetchall()]


def configure(connection):
    connection.execute("SET memory_limit='4GB'")
    connection.execute('SET threads=4')


def verify_file(path, expected_bytes, expected_sha256):
    if not path.is_file():
        raise FileNotFoundError(f'{path} is missing. Run scripts/download_data.py first.')
    if path.stat().st_size != expected_bytes or sha256(path) != expected_sha256:
        raise ValueError(f'{path} differs from the recorded release fingerprint. '
                         'Preserve it and use a different --data-dir for a fresh download.')


def verify_database(connection, args):
    """Reject stale analysis databases before producing summaries."""
    expected = release_catalog()[args.release]
    metadata = connection.execute('SELECT release,csv_sha256 FROM analysis_metadata').fetchall()
    if metadata != [(args.release, expected['csv_sha256'])]:
        raise ValueError('Database provenance differs; rerun scripts/profile_dataset.py.')
    return expected
