# Retail Sales & Returns — Google Data Analytics Case Study

**Ask → Prepare → Process → Analyze → Share → Act** | Python · Pandas · SQL · R · data quality · Power BI modelling

[![Python tests](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/workflows/quality.yml/badge.svg)](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/workflows/quality.yml)
[![Real UCI analysis](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/workflows/uci-evidence.yml/badge.svg)](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/workflows/uci-evidence.yml)

**Verified with the full public dataset on 10 November 2026.** This is an **independent portfolio case study built after completing the Google Data Analytics Professional Certificate**, not a claim that Coursera assessed these exact files.

## Business question

A revenue and operations team needs to understand historic retail sales patterns, leading products and markets, and the quality of the source data. Which results can be trusted, and what further information would be necessary for a decision?

## Real-data findings

<details open><summary>Source-verified historical data analysis</summary>

| Measure | Result | Definition |
|---|---:|---|
| Source transaction lines | **541,909** | Official UCI Online Retail Excel file |
| Valid sale lines | **524,878** | After cleaning and exclusions |
| Distinct sale orders | **19,960** | Unique non-cancelled invoice IDs |
| Gross sales | **£10,642,110.80** | Positive sale lines before costs/returns |
| Average order value | **£533.17** | Gross sales / orders |
| Cancellation line value | **£893,979.73** | Tracked separately, not assumed net refunds |
| Exact duplicate rows | **5,268** | Removed before metric calculations |
| Raw rows missing CustomerID | **135,080** | Flagged rather than invented |

The complete [source-verified executive report](results/uci/README.md) includes the data-quality audit, original-file SHA-256, chart exports, and downloadable aggregate tables. **Pandas and independent SQLite checks agree.**

</details>

![Monthly gross sales — actual UCI historical source](results/uci/charts/monthly_sales.png)

The figures describe a historical UK non-store retailer (2010–2011). They **do not** measure HOK-Elanto, Finnish grocery sales, current consumer behavior or profitability.

## Implementation

- [End-to-end Python pipeline](analysis/pipeline.py): Excel/CSV import, schema validation, deduplication, date/type cleaning, cancellation classification and KPI reports.
- [SQL reconciliation](analysis/sql_checks.sql): count distinct invoices and reconcile gross sales using independent SQL.
- [Automated tests](tests/test_pipeline.py): five regression tests, including end-to-end outputs and SQL/Pandas matching.
- [Real source run](.github/workflows/uci-evidence.yml): downloads official UCI Excel, requires 541,909 source rows, validates metrics and publishes **aggregate results only**.
- [Optional R analysis](analysis/retail_case_study.R) and [Power BI measures](dashboard/POWER_BI_MODEL.md): R not executed; native Power BI .pbix not delivered.
- [Synthetic demonstration](preview/retail_demo_dashboard.svg): separately labelled training fixture, not actual dataset evidence.

## Reproduce the analysis

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python scripts/download_uci.py
python analysis/pipeline.py --input "data/raw/Online Retail.xlsx" --out output/uci
python -m unittest discover -s tests -v
```

For an offline **synthetic** demonstration:

```bash
python scripts/make_demo.py
python analysis/pipeline.py --input data/synthetic_retail_demo.csv --out output/demo
```

## Documentation for reviewers

[Business definitions](docs/DATA_DICTIONARY.md) · [Google capstone mapping](docs/GOOGLE_CAPSTONE_MAPPING.md) · [Reproducibility](docs/REPRODUCIBILITY.md) · [Evidence / provenance](docs/PROJECT_EVIDENCE.md) · [Finnish management summary](docs/JOHDON_YHTEENVETO_FI.md)

**Source and licence:** Daqing Chen (2015), *Online Retail*, UCI Machine Learning Repository, DOI [10.24432/C5BW33](https://doi.org/10.24432/C5BW33), [dataset page](https://archive.ics.uci.edu/dataset/352/online+retail), CC BY 4.0. Original record-level data is downloaded locally, excluded from Git, and not redistributed here.

### Integrity and limitations

- Gross sales are **not** net income, realized profit, or verified revenue net of all refunds.
- Invoice cancellations cannot be matched to original orders from the available fields alone.
- Missing customer IDs limit individual-level customer analysis.
- This is a descriptive, historical case study; causal commercial recommendations need further evidence.

**Code provenance:** COPIED: none from outside repositories. NEW: original analysis code, validation, reporting, tests and CI. ADAPTED: Google's published capstone methodology. INTEGRATED: UCI public source, with attribution. NOT VERIFIED: native Power BI deployment, optional R validation and performance conclusions for any current retailer.
