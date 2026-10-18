# Data dictionary: release 202610

The official CSV has six columns. All are read as strings, including the release value. No field is blank in the downloaded snapshot.

| Column | Meaning | Example or observed values |
|---|---|---|
| `publication_doi` | DOI of the article containing the identified relationship | `10.1371/journal.pone.0012737` |
| `dataset_id` | Referenced DOI or repository accession | `SRR037032` |
| `dataset_id_type` | Identifier system | `DOI`, `accession` |
| `repository` | Accession-source name or DataCite client code | `GenBank/ENA/DDBJ`, `cern.zenodo` |
| `citation_type` | Released pipeline classification | `Primary`, `Secondary`, `Unclassified` |
| `release` | Snapshot month, in YYYYMM form | `202610` |

## Counting units

Each row records an article–identifier relationship. One article may mention many identifiers; one identifier may appear in many articles. Therefore 8,712,962 rows can contain 2,073,909 distinct article DOIs and 4,496,129 distinct raw dataset identifiers.

The upstream internal pipeline works with publication-record IDs. The exported CSV uses publication DOIs. Five exported article DOI–identifier keys have conflicting labels; this exploration retains both rows and reports them. The CSV has no independent row identifier. A cautious provisional dataset key is `(dataset_id_type, repository, dataset_id)`; its uniqueness is descriptive and does not establish conceptual dataset identity.

An accession can identify a run, experiment, sample, study, sequence, structure or reference resource. DOI records can include software, articles and other non-dataset objects. Versions, aliases and parent-child relationships require verified external metadata before aggregation.

## Classification

- **Primary:** classified as data generated for the article.
- **Secondary:** classified as existing data reused by the article.
- **Unclassified:** insufficient evidence to assign either label.

These are algorithmic labels. Unclassified does not mean no reuse. Primary and Secondary are not equivalent to self-citation and third-party reuse. The [published methods](https://github.com/digital-science/ds-make-data-count-pipeline-external/blob/cf5b5c71a3a8ea56e8c02df74568fd0cb28e1a60/docs/methods.md) describe rule, metadata and model-based decisions.

| Identifier type | Primary | Secondary | Unclassified |
|---|---:|---:|---:|
| DOI | 436,943 | 668,336 | 280,987 |
| accession | 1,379,736 | 5,543,944 | 403,016 |

## Filtering and enrichment

Repository, identifier type, classification and release are directly filterable. Repository values mix source names and client codes, so the 2,531 values are not a validated count of independent repositories or disciplines.

Discipline is absent. Article DOIs can be enriched with OpenAlex topics, fields, publication years, venues, authors, affiliations and open-access status. Coverage and inferred topic quality must be measured. Article discipline and the subject of a dataset are distinct attributes. DataCite may provide DOI resource types and subjects; accession-specific repositories can provide organism, experiment and hierarchy metadata. The six-column release has no `is_data_type` flag, rule trace or citation context.

## Repository-count export

[`repository-counts.csv`](../results/202610/repository-counts.csv) has columns `repository`, `value_kind` and `row_count`. It retains each nonmissing repository string exactly as stored, with `value_kind=value`. Three extra rows always report missing categories independently: `missing_null`, `missing_empty_string`, and `missing_whitespace_only`. Their repository cells are blank, and their counts are all zero in this release. These categories partition the rows; their counts plus all ordinary value counts equal 8,712,962.
