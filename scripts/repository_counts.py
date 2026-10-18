"""Count all stored repository values, including three distinct missing categories."""
import csv
import duckdb

from common import arguments, configure, verify_database, write_json


def main():
    args = arguments(__doc__)
    with duckdb.connect(str(args.data_dir / 'profile.duckdb'), read_only=True) as con:
        configure(con)
        verify_database(con, args)
        grouped = con.execute('''SELECT repository, count(*) AS n FROM citations
            GROUP BY repository ORDER BY n DESC, repository''').fetchall()
        total = con.execute('SELECT count(*) FROM citations').fetchone()[0]
    rows = []
    missing = [0, 0, 0]
    for name, n in grouped:
        if name is None:
            missing[0] += n
        elif name == '':
            missing[1] += n
        elif name.isspace():
            missing[2] += n
        else:
            rows.append((name, n))
    if sum(n for _, n in rows) + sum(missing) != total:
        raise ValueError('Repository categories do not reconcile to the row total')
    args.output_dir.mkdir(parents=True, exist_ok=True)
    with (args.output_dir / 'repository-counts.csv').open('w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerow(['repository', 'value_kind', 'row_count'])
        writer.writerows((name, 'value', n) for name, n in rows)
        writer.writerows(('', kind, n) for kind, n in zip(
            ('missing_null', 'missing_empty_string', 'missing_whitespace_only'), missing))
    summary = {'release': args.release, 'total_rows': total,
               'distinct_nonmissing_repository_values': len(rows),
               'missing_null': missing[0], 'missing_empty_string': missing[1],
               'missing_whitespace_only': missing[2]}
    write_json(args.output_dir / 'repository-counts-summary.json', summary)
    print(summary)


if __name__ == '__main__':
    main()
