# Data reuse exploration

Reproducible exploration of the **Digital Science–Make Data Count Open Data Citations** collection, October 2026 release (`202610`). The collection links articles to dataset DOIs and repository accession identifiers and classifies their relationships as Primary, Secondary or Unclassified.

Source: [announcement](https://makedatacount.org/read-our-blog/new-frontier-for-open-data-metrics/), [data/download page](https://makedatacount.org/data-citation/), and [official pipeline and methods](https://github.com/digital-science/ds-make-data-count-pipeline-external). This is the new Digital Science collection, distinct from the older Data Citation Corpus v4.1.

## Observed release

| Measure | Downloaded CSV |
|---|---:|
| Article–identifier rows | 8,712,962 |
| Distinct article DOIs | 2,073,909 |
| Distinct raw dataset identifiers | 4,496,129 |
| Distinct repository/client values | 2,531 |
| Missing repository values | 0 |

Every row has a publication DOI. Articles and identifiers occur in many rows, so distinct article and identifier counts do not add up to the row count. An identifier does not necessarily represent an independent dataset.

The documentation's headline totals are slightly larger; the exact population difference remains unresolved. See [data quality and verified examples](docs/data_quality.md). The numbers above describe the actual downloaded CSV.

## Reproduce the results

Requirements: Python 3.11 or newer (verified with Python 3.12), `curl`, approximately 2 GB free disk space and enough memory for a 4 GB DuckDB limit. Python dependencies are pinned in [requirements.txt](requirements.txt). No Google sign-in or cloud query is required.

From the repository root:

```sh
python -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python scripts/download_data.py
.venv/bin/python scripts/profile_dataset.py
.venv/bin/python scripts/supplemental_analysis.py
.venv/bin/python scripts/repository_counts.py
```

The download is approximately 101 MiB compressed (625 MiB CSV). Downloads use HTTPS with normal TLS verification. The script verifies file sizes and the reference SHA-256 fingerprints in [references/releases.json](references/releases.json), selects the exact CSV member and checks its ZIP CRC on extraction. The fingerprints were computed locally from the official download on 18 October 2026; they are not publisher-issued checksums. An unexpected file is rejected rather than silently replaced or accepted. Verified existing downloads are reused.

Raw data and the DuckDB database live under ignored `data/202610/`. Summaries are written to `results/202610/`. Each script supports `--release`, `--data-dir` and `--output-dir`; use `--help` for details. Defaults are anchored to the repository, so they do not depend on the shell's working directory. Run profiling before the supplemental and repository-count scripts.

To keep a verification run separate from checked-in results, pass the same `--output-dir /path/to/check-results` to all four scripts. The release catalog currently supports `202610` only; later snapshots require a separately recorded source and fingerprint.

## Contents

- [Data dictionary](docs/data_dictionary.md): columns, classifications, row meaning and filtering limits.
- [Data quality](docs/data_quality.md): parser checks, count discrepancy, repeated keys and validated examples.
- [Completed reproduction checks](docs/reproduction.md): full runs, comparison and missing-value verification.
- [Complete repository counts](results/202610/repository-counts.csv): all values plus explicit missing categories; [summary](results/202610/repository-counts-summary.json).
- [Profile](results/202610/profile.json) and [additional checks](results/202610/supplemental-profile.json).
- [Annotated bibliography](docs/literature.md): ten relevant papers, reading depth and methodological implications; [metadata](references/papers.json).
- [Draft research directions](notes/research-directions.md): proposals retained for discussion, not a chosen research plan.

The scripts retain the raw records. They use explicit standard CSV quoting and strict parsing, validate the input fingerprint, and independently check the CSV with Python's CSV reader. Repository-count categories reconcile to the total row count. The five repeated article–identifier keys with conflicting labels are reported rather than resolved automatically.

## Interpretation and attribution

The CSV records observed links, not a complete inventory of all datasets or all scientific reuse. It has no author identities, disciplines, article dates, citation contexts, downloads or views. `release` is the snapshot month, not the date of a reuse event. Secondary is a pipeline classification, not independently established third-party analytical reuse.

Original analysis code is covered by the existing [MIT license](LICENSE). The upstream dataset is released under CC0, as stated on its official landing page. Source articles and other third-party material retain their own terms; downloaded paper full texts, copied upstream code and web-page caches are excluded. Bibliographic and validation notes link to their sources. See [source provenance](references/sources.json).
