# Draft research directions

Status: exploratory proposals, not a selected study design or established findings. A focused novelty review and an agreed study population are needed before pursuing a paper.


### 1. How much do identifier hierarchy and granularity change apparent data reuse?

**Question:** Do repository and dataset impact rankings change when we count run, experiment, sample, study and version identifiers separately versus through explicit hierarchical relationships?

**Starting evidence:** The verified SRR/SRX pair shows both a run and its parent experiment in one article. The file contains 147,245 rows with canonical SRA/ENA/DDBJ run/experiment/study/sample prefixes matching `[SED]R[RSXP]`, providing a bounded initial population; that pattern is a screening rule, not a complete inventory of sequencing data.

**Design:** Resolve hierarchy in a documented SRA subset with ENA/NCBI metadata, retain typed nodes, then compare unique article–identifier, article–experiment and article–study counts. Report Primary, Secondary and Unclassified separately. Test changes in concentration and rankings under each counting unit, with manually checked mappings and uncertainty for unresolved records. Extend to GEO or DOI versions only after defining their distinct relationship semantics.

**Potential contribution:** An empirical evaluation of what a large data-reuse indicator is counting, plus reusable aggregation guidance. This is more substantive than simply ranking the most cited identifiers. Silvello, Belter and Khan et al. provide conceptual and empirical precedents in the [bibliography](../docs/literature.md).

**Limits and next decision:** Parent-child links do not imply interchangeable data; collapsing an entire study could conceal genuinely distinct reuse. The exact overlap prevalence and ranking effects have not been measured. A pilot scope and aggregation definition should be agreed before broad metadata harvesting.

### 2. How robust are reuse indicators to object type and classifier provenance?

**Question:** Which conclusions about reused data survive filtering non-data DOI objects, accounting for Unclassified links and excluding inference rules that encode the metric being studied?

**Starting evidence:** The verified Article/Text object is present in the public file. The published method uses popularity, author/date matching and earliest-citer rules; some later citations are demoted from Primary by design. Consequently, comparisons involving popularity, first reuse or team overlap may partly reproduce classifier assumptions.

**Design:** Define alternative, transparent counting specifications; enrich DOI resource types; use trace tables to stratify by rule/evidence tier; and independently annotate a stratified article-context sample. Compare repository rankings, concentration and estimated label precision across these specifications. Keep supplied rule precision distinct from an independent gold standard. Treat exclusion of a rule as a sensitivity analysis, not proof the remaining labels are correct.

**Potential contribution:** A measurement-validity paper showing the direction and magnitude of indicator sensitivity, grounded in an independent audit. Piwowar & Vision, Park & Wolfram, Pasquetto and Cousijn et al. clarify why citations, own-data creation, third-party reuse and usage are different constructs.

**Limits and next decision:** The headline benchmark is agreement on a small overlapping gold set, not a corpus-wide accuracy estimate; documentation says GenBank coverage is poor. The CSV cannot expose decision rules. A deeper provenance audit requires richer public tables or independent source reconstruction, and an agreed annotation design.

### 3. Which data use is visible in formal citations versus article prose and tables?

**Question:** What changes in measured data impact when we include identifier mentions in body text, tables and availability statements rather than relying on bibliographic references or registered article–data relations?

**Starting evidence:** The source article for the SRR/SRX case exposes different identifier levels in prose and a table. The pipeline's reproducibility layer documents mention locations and provides sentence text for open-access articles. Belter, Park & Wolfram and Khan et al. document inconsistent citation and reuse practices in earlier collections.

**Design:** Within a clearly defined set of accessible articles, compare matched identifier links from references, availability statements, prose and tables with registered relations. Manually code whether a mention supports new-data deposition, analytical reuse, background use or an ambiguous relationship. Measure differences by identifier type and repository; avoid assuming the location itself determines reuse.

**Potential contribution:** A study of which forms of data use conventional citation indicators omit, with a validated context taxonomy rather than another aggregate citation count.

**Limits and next decision:** The six columns do not include context, dates or disciplines. Source XML can be obtained for some open articles; fuller coverage needs the trace layer. Results must be limited to the analyzed full-text population. Missing links do not establish no reuse, and an open-access subset is not a representative sample of all science.
