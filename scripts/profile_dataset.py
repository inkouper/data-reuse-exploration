"""Profile every row of the verified CSV and build a local analysis database."""
import duckdb

from common import (COLUMNS, arguments, configure, query, release_catalog, verify_file,
                    write_json)

checks = {
    'summary': '''SELECT count(*) AS n_rows, count(DISTINCT publication_doi) articles,
        count(DISTINCT dataset_id) dataset_ids, count(DISTINCT repository) repositories,
        count(DISTINCT (dataset_id_type,repository,dataset_id)) repository_scoped_ids,
        count(*)-count(DISTINCT (publication_doi,dataset_id)) duplicate_article_id_pairs
        FROM citations''',
    'schema': 'DESCRIBE citations',
    'null_counts': 'SELECT ' + ','.join(f"count(*) FILTER (WHERE {c} IS NULL OR trim({c})='') AS {c}" for c in ['publication_doi','dataset_id','dataset_id_type','repository','citation_type','release']) + ' FROM citations',
    'release': 'SELECT release, count(*) AS n_rows FROM citations GROUP BY ALL ORDER BY release',
    'types': 'SELECT dataset_id_type,citation_type,count(*) AS n_rows,count(DISTINCT publication_doi) articles,count(DISTINCT dataset_id) ids FROM citations GROUP BY ALL ORDER BY 1,2',
    'repositories': 'SELECT repository,dataset_id_type,count(*) AS n_rows,count(DISTINCT publication_doi) articles,count(DISTINCT dataset_id) ids,count(*) FILTER (WHERE citation_type=\'Primary\') primary_rows,count(*) FILTER (WHERE citation_type=\'Secondary\') secondary_rows,count(*) FILTER (WHERE citation_type=\'Unclassified\') unclassified_rows FROM citations GROUP BY 1,2 ORDER BY n_rows DESC, repository, dataset_id_type',
    'top_identifiers': 'SELECT dataset_id_type,repository,dataset_id,count(*) AS n_rows,count(*) FILTER (WHERE citation_type=\'Secondary\') secondary_rows FROM citations GROUP BY ALL ORDER BY n_rows DESC, dataset_id_type, repository, dataset_id LIMIT 30',
    'article_identifier_histogram': 'SELECT n_ids,count(*) articles FROM (SELECT publication_doi,count(*) n_ids FROM citations GROUP BY 1) GROUP BY 1 ORDER BY 1',
    'identifier_article_histogram': 'SELECT n_articles,count(*) ids FROM (SELECT dataset_id_type,repository,dataset_id,count(DISTINCT publication_doi) n_articles FROM citations GROUP BY 1,2,3) GROUP BY 1 ORDER BY 1',
    'label_mixing': '''SELECT dataset_id_type,count(*) identifiers,
        count(*) FILTER (WHERE p>0 AND s>0) primary_and_secondary,
        count(*) FILTER (WHERE p>1) multiple_primary_papers,
        count(*) FILTER (WHERE p=0 AND s>0) secondary_without_primary
        FROM (SELECT dataset_id_type,repository,dataset_id,
        count(DISTINCT publication_doi) FILTER (WHERE citation_type='Primary') p,
        count(DISTINCT publication_doi) FILTER (WHERE citation_type='Secondary') s
        FROM citations GROUP BY 1,2,3) GROUP BY 1 ORDER BY 1''',
    'cross_repository_ids': '''SELECT count(*) ids_with_multiple_repository_codes FROM
        (SELECT dataset_id_type,dataset_id,count(DISTINCT repository) n FROM citations GROUP BY 1,2 HAVING n>1)''',
}

def main():
    args = arguments(__doc__)
    spec = release_catalog()[args.release]
    csv_path = args.data_dir / spec['csv_member']
    verify_file(csv_path, spec['csv_bytes'], spec['csv_sha256'])
    with duckdb.connect(str(args.data_dir / 'profile.duckdb')) as con:
        configure(con)
        con.execute("""CREATE OR REPLACE TABLE citations AS SELECT * FROM
            read_csv(?, header=true, all_varchar=true, delim=',', quote='"', escape='"',
                     strict_mode=true, ignore_errors=false)""", [str(csv_path)])
        if [x[0] for x in con.execute('DESCRIBE citations').fetchall()] != COLUMNS:
            raise ValueError('CSV header differs from the documented six columns')
        if con.execute('SELECT DISTINCT release FROM citations').fetchall() != [(args.release,)]:
            raise ValueError('CSV contains an unexpected or missing release value')
        con.execute('CREATE OR REPLACE TABLE analysis_metadata (release VARCHAR,csv_sha256 VARCHAR)')
        con.execute('INSERT INTO analysis_metadata VALUES (?,?)', [args.release,spec['csv_sha256']])
        results = {'duckdb_version': duckdb.__version__, 'release': args.release,
                   'input_csv_sha256': spec['csv_sha256']}
        for name, sql in checks.items():
            results[name] = query(con, sql)
            print(name, results[name][:1], flush=True)
    write_json(args.output_dir / 'profile.json', results)


if __name__ == '__main__':
    main()
