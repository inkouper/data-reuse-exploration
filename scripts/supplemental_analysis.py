"""Check pair keys, self-links, identifier prefixes and independent CSV parsing."""
import csv
import duckdb

from common import (COLUMNS, arguments, configure, query, verify_database, verify_file,
                    write_json)


def main():
    args = arguments(__doc__)
    with duckdb.connect(str(args.data_dir / 'profile.duckdb'), read_only=True) as con:
        configure(con)
        spec = verify_database(con, args)
        csv_path = args.data_dir / spec['csv_member']
        verify_file(csv_path, spec['csv_bytes'], spec['csv_sha256'])
        def q(sql):
            return query(con, sql)
        out={
         'repeated_pair_keys': q('SELECT publication_doi,dataset_id,count(*) AS n,list(citation_type ORDER BY citation_type) AS labels FROM citations GROUP BY 1,2 HAVING count(*)>1 ORDER BY 1,2'),
         'exact_duplicate_rows': q('SELECT *, count(*) AS n FROM citations GROUP BY ALL HAVING count(*)>1 ORDER BY publication_doi,dataset_id'),
         'self_doi_edges': q("SELECT citation_type,count(*) AS n_rows FROM citations WHERE dataset_id_type='DOI' AND lower(publication_doi)=lower(dataset_id) GROUP BY 1 ORDER BY 1"),
         'verified_examples': q("SELECT * FROM citations WHERE (publication_doi='10.11576/dimawe-4862' AND dataset_id='10.11576/dimawe-4862') OR (publication_doi='10.1371/journal.pone.0012737' AND dataset_id IN ('SRR037032','SRX017250')) ORDER BY publication_doi,dataset_id"),
         'sra_identifier_prefixes': q("SELECT regexp_extract(dataset_id,'^[A-Za-z]+') AS prefix,count(*) AS n_rows,count(DISTINCT dataset_id) AS identifiers FROM citations WHERE regexp_matches(dataset_id,'^[SED]R[RSXP][0-9]+$') GROUP BY 1 ORDER BY n_rows DESC, prefix"),
         'publication_prefixes': q("SELECT split_part(publication_doi,'/',1) AS doi_prefix,count(*) AS n_rows FROM citations GROUP BY 1 ORDER BY n_rows DESC, doi_prefix LIMIT 15"),
        }
        expected_rows = con.execute('SELECT count(*) FROM citations').fetchone()[0]
    with csv_path.open(newline='', encoding='utf-8') as f:
        reader = csv.reader(f, strict=True)
        header = next(reader)
        n = bad = 0
        for row in reader:
            n += 1
            bad += len(row) != len(COLUMNS)
    if header != COLUMNS or bad or n != expected_rows:
        raise ValueError(f'Independent CSV check failed: rows={n}, malformed={bad}')
    out['stdlib_csv_check'] = {'header': header, 'data_rows': n,
                               'rows_with_wrong_field_count': bad}
    write_json(args.output_dir / 'supplemental-profile.json', out)
    write_json(args.output_dir / 'repeated-pair-keys.json', out['repeated_pair_keys'])
    for name, value in out.items():
        print(name, value[:1] if isinstance(value,list) else value, flush=True)


if __name__ == '__main__':
    main()
