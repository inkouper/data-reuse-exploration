# Ten prominent papers on data reuse and its indicators

Prepared 18 October 2026 for research with the **Digital Science–Make Data Count Open Data Citations, release 202610**. This is a focused, verified reading list, not a systematic review. The dataset description used here is the documented six-column release: `publication_doi`, `dataset_id`, `dataset_id_type`, `repository`, `citation_type`, `release`, with Primary/Secondary/Unclassified labels and both DOI and repository-accession identifiers. The exploration downloaded and profiled the full official CSV: **8,712,962 rows, 2,073,909 unique publication DOIs, and 4,496,129 distinct raw dataset IDs**. These are file observations; the slightly larger counts in the release documentation describe a population whose difference is not yet fully reconciled. See [measured profile](../results/202610/profile.json) and [inspected record examples and count reconciliation](data_quality.md).

## Selection and evidence

Selection prioritizes direct relevance to measuring reuse and citation, foundational influence, explicit methods, and complementary perspectives: accession-based reuse, citation validity, counting units, infrastructure coverage, behavioral determinants and citation incentives. Reading order favors practical relevance to this corpus; it is not a ranking by quality. All ten are scholarly journal publications; the conceptual essay is identified as such. No blog posts or repository documentation count toward the ten.

Prominence is supported by an OpenAlex snapshot retrieved 18 October 2026 (23–611 citing works across these papers). Counts are database-dependent, change over time, favor older publications and do not establish validity. Bibliographic metadata, source links, dated citation-count observations and annotations are in [`references/papers.json`](../references/papers.json). Full-text and API response caches remain local and are not included in this repository. Publisher pages, Europe PMC full text, and open author manuscripts were consulted as identified below. Two papers were read only at publisher-abstract level. Issue years are used for Robinson-García et al. (2016; online 2015) and Silvello (2018; online 2017).

## Reading list

### 1. Data reuse and the open data citation advantage

Heather A. Piwowar; Todd J. Vision (2013). *PeerJ*, 1, e175. [10.7717/peerj.175](https://doi.org/10.7717/peerj.175).

**Type and prominence:** Empirical observational study; OpenAlex cited-by count 611 on 18 October 2026 ([record](https://openalex.org/W2045657963)).

**What it contributes:** Analyzes 10,555 gene-expression studies; distinguishes article citation advantage from accession-attributed third-party reuse. Adjusted citation association is about 9%. Authors inspect citation contexts and identify reuse through GEO/ArrayExpress accessions and depositor/citing-author surname overlap.

**Why it matters here:** The closest methodological precedent for mixed DOI/accession corpus links and for separating investigator reuse from third-party reuse.

**Concrete question:** Among links labelled Secondary, what fraction actually describe third-party analysis rather than mere mention, and how do accession and DOI records differ?

**Design and limits:** Count distinct publication–dataset edges by dataset_id_type and repository; validate a stratified sample using article contexts. Author overlap and time-to-reuse require author/date metadata enrichment. Surname overlap is imperfect; do not equate Secondary with third-party reuse.

**Read depth:** Full text: methods, reuse operationalization, results and limitations inspected.

### 2. Bringing Citations and Usage Metrics Together to Make Data Count

Helena Cousijn; Patricia Feeney; Daniella Lowenberg; Eleonora Presani; Natasha Simons (2019). *Data Science Journal*, 18, 9. [10.5334/dsj-2019-009](https://doi.org/10.5334/dsj-2019-009).

**Type and prominence:** Infrastructure and methods paper; OpenAlex cited-by count 83 on 18 October 2026 ([record](https://openalex.org/W2920085759)).

**What it contributes:** Explains how Scholix article–data links and standardized COUNTER data usage metrics can be exposed together. It treats citation and usage as complementary dimensions; views/investigations and downloads/requests require defined counting rules.

**Why it matters here:** Direct intellectual foundation for Make Data Count. The released six-column corpus provides publication–dataset links, not standardized views/downloads.

**Concrete question:** How much do repository-level interpretations of data impact change when citation indicators are compared with standardized usage indicators?

**Design and limits:** Corpus can supply link counts and Secondary shares by repository. Answering the comparison requires separately available, compatible usage reports; downloads still do not prove scientific reuse.

**Read depth:** Publisher full text: conceptual framing, Scholix, COUNTER and limitations inspected.

### 3. Measuring the Value of Research Data: A Citation Analysis of Oceanographic Data Sets

Christopher W. Belter (2014). *PLoS ONE*, 9(3), e92590. [10.1371/journal.pone.0092590](https://doi.org/10.1371/journal.pone.0092590).

**Type and prominence:** Empirical measurement case study; OpenAlex cited-by count 88 on 18 October 2026 ([record](https://openalex.org/W2172222848)).

**What it contributes:** Attempts to count citations and mentions to three curated oceanographic datasets using Web of Science, publisher full-text search and Google Scholar. Finds inconsistent citation forms despite recommended formats and demonstrates the importance of multiple detection routes.

**Why it matters here:** Supports a measurement audit of DOI-only versus accession-inclusive indicators and warns that counts depend on search coverage and what counts as a citation.

**Concrete question:** How sensitive are apparent dataset and repository impact rankings to identifier type, mention detection and duplicate counting?

**Design and limits:** Compare publication counts, distinct identifier counts and distinct edges by dataset_id_type/repository; trace selected source articles where available. Entity merging requires verified aliases; do not assume several accessions represent several independent datasets.

**Read depth:** Full text: search/counting methods, findings and interpretation inspected.

### 4. An examination of research data sharing and re-use: implications for data citation practice

Hyoungjoo Park; Dietmar Wolfram (2017). *Scientometrics*, 111(1), 443-461. [10.1007/s11192-017-2240-2](https://doi.org/10.1007/s11192-017-2240-2).

**Type and prominence:** Empirical exploratory case study; OpenAlex cited-by count 54 on 18 October 2026 ([record](https://openalex.org/W2582647261)).

**What it contributes:** Examines Genetics and Heredity citation practices using the Data Citation Index and 148 sampled citing articles. Its citer-based approach considers formal and implicit citations, self-citation, main text, supplements, acknowledgments and author information.

**Why it matters here:** Provides a concrete precedent for validation using citing articles rather than trusting index-level citation counts.

**Concrete question:** Does the meaning and accuracy of a Secondary label vary by repository, identifier system and citation location?

**Design and limits:** Draw a stratified sample using repository, dataset_id_type and citation_type; inspect source context and independently annotate actual reuse. The paper abstract supports the design, not unverified numerical outcomes or a claim of classifier accuracy.

**Read depth:** Publisher abstract and bibliographic metadata only; subscription full text not accessed.

### 5. Analyzing data citation practices using the data citation index

Nicolas Robinson‐García; Evaristo Jiménez‐Contreras; Daniel Torres‐Salinas (2016). *Journal of the Association for Information Science and Technology*, 67(12), 2964-2975. [10.1002/asi.23529](https://doi.org/10.1002/asi.23529).

**Type and prominence:** Empirical bibliometric coverage study; OpenAlex cited-by count 109 on 18 October 2026 ([record](https://openalex.org/W2135980511)).

**What it contributes:** Analyzes Data Citation Index records by field, object type and repository. Reports that 88.1% of records in its historical DCI sample were uncited, with substantial variation across repositories and disciplines.

**Why it matters here:** Shows how infrastructure coverage and repository/object conventions shape measured citation activity. Its uncitedness result cannot be transferred to a corpus containing observed citation edges.

**Concrete question:** Which apparent cross-repository differences persist after separating object types and accounting for index coverage?

**Design and limits:** Use repository and dataset_id_type to describe observed edges; attach verified dataset/object metadata for stratified comparisons. Uncitedness and reuse rates need a separate inventory of all eligible datasets, including those absent from the corpus.

**Read depth:** Crossref abstract plus openly available author manuscript: methods, repository coverage and discussion inspected.

### 6. Theory and practice of data citation

Gianmaria Silvello (2018). *Journal of the Association for Information Science and Technology*, 69(1), 6-20. [10.1002/asi.23917](https://doi.org/10.1002/asi.23917).

**Type and prominence:** Conceptual and technical review; OpenAlex cited-by count 121 on 18 October 2026 ([record](https://openalex.org/W2686965047)).

**What it contributes:** Synthesizes the purposes and technical problems of data citation, including identification, attribution, fixity, provenance, variable granularity, versions and dynamic datasets. Persistent identifiers alone do not solve subset/version identification.

**Why it matters here:** Explains why dataset_id is an identifier unit rather than automatically an independent conceptual dataset, and why accession/DOI comparisons need entity-resolution rules.

**Concrete question:** How much do impact concentration and repository rankings change when records are counted as identifiers, versions, dataset families or collections?

**Design and limits:** Start from (dataset_id_type, repository, dataset_id) as a cautious provisional key; enrich with verified parent/version/alias relations before aggregation. Publish sensitivity analyses rather than silently collapsing distinct entities.

**Read depth:** Crossref abstract plus openly available accepted manuscript: identification, granularity and provenance sections inspected.

### 7. On the Reuse of Scientific Data

Irene V. Pasquetto; Bernadette M. Randles; Christine L. Borgman (2017). *Data Science Journal*, 16, 8. [10.5334/dsj-2017-008](https://doi.org/10.5334/dsj-2017-008).

**Type and prominence:** Peer-reviewed conceptual essay; OpenAlex cited-by count 237 on 18 October 2026 ([record](https://openalex.org/W2598446296)).

**What it contributes:** Explains why making data available is different from achieving reuse, and why use/reuse boundaries depend on actors, purposes, provenance and scientific context. Proposes six research questions about reuse, reproducibility, integration and release practices.

**Why it matters here:** Provides construct validity for interpreting Primary/Secondary/Unclassified labels: a link or label is evidence about an article–data relationship, not a complete account of what researchers did.

**Concrete question:** Which forms of reuse—replication, integration, novel analysis or method testing—are represented by Secondary links, and which are missed?

**Design and limits:** The six released columns cannot identify reuse purpose. Context-based manual coding, potentially assisted by trace information, can produce an explicit reuse taxonomy and measured agreement with corpus labels.

**Read depth:** Publisher full text: conceptual framework and research questions inspected.

### 8. Attitudes and norms affecting scientists’ data reuse

Renata Gonçalves Curty; Kevin Crowston; Alison Specht; Bruce W. Grant; Elizabeth D. Dalton (2017). *PLOS ONE*, 12(12), e0189288. [10.1371/journal.pone.0189288](https://doi.org/10.1371/journal.pone.0189288).

**Type and prominence:** Empirical survey and theory-testing study; OpenAlex cited-by count 116 on 18 October 2026 ([record](https://openalex.org/W2781265499)).

**What it contributes:** Uses DataONE survey responses and the Theory of Reasoned Action to study self-reported reuse. Perceived efficacy, efficiency and importance are associated with reuse behavior; perceived distrust and norms against reuse were not major impediments in the tested model.

**Why it matters here:** Adds behavioral dimensions that citation records do not observe, preventing a study of scholarly links from being presented as a complete study of researcher motivations.

**Concrete question:** Do the communities with high observed Secondary-link activity also report benefits and practices associated with reuse?

**Design and limits:** Corpus can motivate community selection only after field enrichment. Testing motivations needs a survey or interview component, subject to a separate study decision and any ethics requirements; repository identity is not a behavioral measure.

**Read depth:** Full text: behavioral model, measures, results and limitations inspected.

### 9. Measuring the impact of biodiversity datasets: data reuse, citations and altmetrics

Nushrat Khan; Mike Thelwall; Kayvan Kousha (2021). *Scientometrics*, 126(4), 3621-3639. [10.1007/s11192-021-03890-6](https://doi.org/10.1007/s11192-021-03890-6).

**Type and prominence:** Empirical bibliometric and content-analysis study; OpenAlex cited-by count 23 on 18 October 2026 ([record](https://openalex.org/W3134155190)). Included for its particularly close methodological fit and more recent domain evidence; it is less highly cited than the foundational papers.

**What it contributes:** Studies openly available metadata for 43,802 GBIF datasets and content-codes 100 randomly sampled citing articles. Finds varied background and foreground reuse, inconsistent citation practice when many subsets are used, and altmetric mentions that often point to associated articles rather than datasets.

**Why it matters here:** Provides a newer, directly relevant empirical template combining large-scale dataset metadata with a small interpretable context audit; explicitly addresses subset aggregation and proxy validity.

**Concrete question:** Among GBIF or comparable repository links, which Secondary relationships reflect foreground analytical reuse, background use or software testing, and how does counting many subsets affect apparent impact?

**Design and limits:** Use repository to select a documented subgroup, then annotate a stratified sample and report both distinct publications and distinct dataset identifiers. The corpus has no altmetrics or article contexts; those require enrichment. Foreground/background is a separate taxonomy from Primary/Secondary and must not be mapped automatically.

**Read depth:** Publisher abstract and bibliographic metadata only; subscription full text not accessed.

### 10. The citation advantage of linking publications to research data

Giovanni Colavizza; Iain Hrynaszkiewicz; Isla Staden; Kirstie Whitaker; Barbara McGillivray (2020). *PLOS ONE*, 15(4), e0230416. [10.1371/journal.pone.0230416](https://doi.org/10.1371/journal.pone.0230416).

**Type and prominence:** Large empirical observational study; OpenAlex cited-by count 334 on 18 October 2026 ([record](https://openalex.org/W2955244474)).

**What it contributes:** Analyzes 531,889 PLOS/BMC articles, categorizing data availability statements. Repository-linked statements are associated with up to 25.36% higher article citation impact under its models; the paper discusses selection, coverage and other limitations.

**Why it matters here:** A stronger-scale comparison for citation-advantage research, while preserving the distinction between data availability statements, article citations and dataset reuse.

**Concrete question:** Are Secondary links associated with later article visibility beyond the presence of a repository-linked availability statement?

**Design and limits:** Requires DAS text/categories, article citation outcomes, publication-year and venue/field controls, and an eligible article denominator. Use observational language and consider reverse timing and selection; release is a corpus version, not article publication year.

**Read depth:** Full text: DAS categories, citation models, findings and limitations inspected.

## Connections to inspected corpus records

The [record audit](data_quality.md) makes the measurement issues concrete. The parent profile found 6,743 self-DOI edges (the publication DOI equals the cited identifier). One inspected DOI, `10.11576/dimawe-4862`, is registered by DataCite as Article/Text rather than Dataset, despite appearing as a Primary link. This supports an object-type validity audit; it does not establish that all self-DOI edges are errors or estimate the prevalence of non-data objects. Belter and Park motivate checking what an indexed relationship actually represents.

For publication `10.1371/journal.pone.0012737`, the CSV separately records run `SRR037032` as Primary and its parent experiment `SRX017250` as Unclassified; an ENA response confirms their relationship. This directly illustrates Silvello’s distinction between identifiers, granularity and conceptual data objects. It also motivates checking classification consistency across related identifiers, with the article context required to decide whether the two links concern the same passage or distinct uses. This is an inspected example, not a measured corpus-wide rate.

## What this bibliography permits us to claim

The strongest initial paper design is a study of **measurement validity and indicator sensitivity**: test how interpretations and rankings change with citation labels, identifier types, counting units and repository coverage, then validate a stratified sample against article contexts. Piwowar & Vision, Belter, Park & Wolfram, Robinson-García and Silvello provide direct precedents. Pasquetto defines the construct being measured; Cousijn establishes why citation links and usage metrics should remain distinct. This is a recommendation for consideration, not a decision to choose the project.

Count distinct publications per provisional dataset key and distinct publication–dataset edges, report Primary/Secondary/Unclassified separately, and show how conclusions change under documented deduplication or verified entity aggregation. Preserve the raw rows. Secondary is a released classification and a useful sampling stratum; it is not independently validated reuse or proof that the authors differ from the original data producers.

An observed citation edge supports a statement about an indexed relationship. It does not by itself establish that data were accessed, analyzed, reproduced, integrated, successfully reused, or reused by a third party. Neither absence of a link nor an Unclassified label proves no reuse. Downloads/views, when later available, are also imperfect proxies.

The six columns contain no author identities, article/dataset dates, subject fields, citation contexts, FAIR scores, download counts or inventory of uncited datasets. `release` identifies the corpus release, not when reuse happened. Time-to-reuse, interdisciplinary diffusion, actual third-party reuse and metadata/FAIR associations require explicit enrichment. Uncitedness, reuse probability, or a causal effect of sharing require appropriate denominators and additional design. Primary labels must not automatically be interpreted as self-citations.

Several attractive studies therefore exceed the released file alone: citation-advantage replication needs article outcomes and unlinked comparison articles; views-versus-citations needs compatible usage reports; behavioral determinants need human-subject research. The cited observational papers support careful associations, not claims that sharing causes citations or that repository choice causes reuse.

## Search and reproducibility notes

Searched Crossref title metadata for known directly relevant works, checked exact DOI records, used Europe PMC for five open empirical papers, publisher pages for two Data Science Journal papers and the Park and Khan abstracts, and openly available author manuscripts for the two JASIST papers. OpenAlex DOI lookups independently confirmed metadata and supplied prominence counts. A brief additional Crossref search for recent data-reuse/indicator papers identified the directly relevant 2021 GBIF study, which was included in place of a redundant early citation-advantage study. A 2025 Data Citation Corpus meeting abstract was not selected because it supplies neither a full research article nor a stronger methodological foundation. This selected bibliography covers influential measurement foundations through 2021; it does not claim an exhaustive search of newer literature or that any proposed project is novel. A focused novelty search is necessary after the user chooses a research direction.

Evidence sources: Crossref `https://api.crossref.org/works/{doi}`; OpenAlex `https://api.openalex.org/works/https://doi.org/{doi}`; Europe PMC `https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML`; publisher DOI landing pages; arXiv author manuscripts 1706.07976 (Silvello) and 1501.06285 (Robinson-García et al.). No accounts, payment, external postings or large dataset downloads were used.