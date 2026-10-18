# Data quality and verified examples

Observations refer to the public CSV downloaded on 18 October 2026. These checks describe that file and selected records, not corpus-wide classification accuracy.

## Input and parsing

The archive is 105,731,352 bytes and the data CSV member is 654,613,481 bytes. The ZIP also contains a macOS `._*.csv` metadata file; the downloader selects only `data_citations_202610.csv`. Reference fingerprints are recorded in [releases.json](../references/releases.json) and the generated [download manifest](../results/202610/download-manifest.json). These are locally computed fingerprints, not publisher-provided checksums.

DuckDB parses all six columns with explicit comma delimiters and double-quote escaping, strict mode and no ignored errors. Python's independent strict CSV reader agrees on 8,712,962 rows and finds no wrong field counts. All six columns are nonblank, and every row carries release `202610`.

## Documentation versus CSV counts

| Measure | Official methods headline | Downloaded CSV |
|---|---:|---:|
| Citation rows | 8,751,192 | 8,712,962 |
| Articles/publication identifiers | 2,081,909 | 2,073,909 |
| Dataset identifiers | 4,508,541 | 4,496,129 |

The differences are 38,230 rows, 8,000 publication identifiers and 12,412 dataset identifiers. The README says articles without DOI are excluded from the released data, while the internal product and SRAD release aggregates use publication-record IDs. This supports a population difference as a possible explanation. The exact export query and internal release rows were not available for comparison, so the entire difference remains unreconciled. The checked-in results consistently use the measured CSV counts.

Sources at upstream commit `cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60`: [README](https://github.com/digital-science/ds-make-data-count-pipeline-external/blob/cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60/README.md), [internal product](https://github.com/digital-science/ds-make-data-count-pipeline-external/blob/cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60/sql/70_data_citations_view.sql), [SRAD citations](https://github.com/digital-science/ds-make-data-count-pipeline-external/blob/cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60/sql/73_srad_citations.sql), [release aggregates](https://github.com/digital-science/ds-make-data-count-pipeline-external/blob/cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60/sql/76_srad_releases.sql).

## Repeated keys and object types

There are no exact duplicate six-column rows. Five article DOI–dataset identifier pairs occur twice with conflicting Primary/Secondary or Secondary/Unclassified labels. They are retained and listed in [repeated-pair-keys.json](../results/202610/repeated-pair-keys.json); the scripts do not choose a preferred label.

There are 6,743 DOI rows where publication DOI equals dataset DOI: 6,680 Primary, 11 Secondary and 52 Unclassified. This is a screening observation, not a measured error rate. One verified example is `10.11576/dimawe-4862`, present as both article and dataset DOI with label Primary. Its [DataCite metadata](https://api.datacite.org/dois/10.11576/dimawe-4862) classifies it as Article/Text/ScholarlyArticle. This confirms one non-data object in the public file. The six-column CSV does not expose the `is_data_type` flag recommended by the methods; analyses restricted to dataset objects require enrichment.

## A verified accession hierarchy

Article DOI `10.1371/journal.pone.0012737` has records for `SRR037032` (Primary) and `SRX017250` (Unclassified), both under `GenBank/ENA/DDBJ`. [ENA](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR037032&result=read_run&fields=run_accession,experiment_accession,sample_accession,study_accession,secondary_study_accession&format=tsv) resolves the run to that experiment, sample `SAMN00009490`, and study `PRJNA79573` / `SRP002028`.

The [open article](https://doi.org/10.1371/journal.pone.0012737) names the experiment in prose; Table 4 contains experiment `SRX017250.1` and run `SRR037032.2`. The exported identifiers are unversioned. This establishes an actual parent-child overlap and different mention locations. It does not establish overlap prevalence, an overcount of Secondary reuse, or that all related identifiers should be collapsed. Unclassified asserts neither creation nor reuse.

The three inspected release rows are in [record-examples.csv](../results/202610/record-examples.csv). Lookup URLs and selected metadata observations are preserved in [record-lookups.json](../references/record-lookups.json). Raw paper full texts and web caches are not redistributed.

## Interpretation boundaries

The corpus contains observed edges, not all eligible datasets or all articles. It cannot establish uncitedness or the probability of reuse without external denominators. It does not contain usage counts, article dates, researcher motivations or reuse purposes. Citation labels depend partly on popularity, author/date matching and earliest-citer rules, so studies of those same properties need provenance-aware sensitivity analyses. The documented benchmark is agreement on an overlapping gold set, not an independent accuracy estimate for every repository family.
