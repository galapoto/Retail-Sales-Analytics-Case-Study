# Source, implementation and verification evidence

**Last verified:** 10 November 2026. **Public repository:** https://github.com/galapoto/Retail-Sales-Analytics-Case-Study

## Verified deployment results

- **Published code:** end-to-end data cleansing, KPI calculation, SQL cross-check, charts and reporting.
- **Python unit tests:** 5/5 passed locally and on GitHub Actions.
- **Official source analysis:** GitHub Actions run [42759973718](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/runs/42759973718) completed successfully.
- **Real source:** 541,909 transaction rows, source SHA-256 `43465a06f2ccf7c8b5bd2892bc7defb52f97487934fe93b16ae4c3936424676d`.
- **SQL verification:** 19,960 unique sale orders and £10,642,110.80 gross sales reconciled with Pandas.
- **Public evidence:** [results/uci/README.md](../results/uci/README.md), source provenance JSON, audit JSON, monthly/country/product CSV tables and PNG charts.
- **Source details:** Daqing Chen, 2015, UCI Online Retail, CC BY 4.0, DOI 10.24432/C5BW33.

## Exact code provenance

- **COPIED:** none. No third-party project source code imported; the target repository started empty.
- **NEW:** analysis/pipeline.py, tests/test_pipeline.py, scripts/make_demo.py, scripts/download_uci.py, scripts/publish_uci_evidence.py, scripts/make_preview.py, analysis/sql_checks.sql, analysis/retail_case_study.R and all code CI.
- **ADAPTED:** methodology from Google's publicly described Ask → Prepare → Process → Analyze → Share → Act capstone workflow.
- **INTEGRATED:** authoritative UCI source downloaded at workflow execution; only aggregated outputs published. The original 541,909-row source remains out of version control.
- **LOCALLY TESTED:** Python test suite PASS. Evidence-publishing script passed a synthetic-input smoke test with explicitly overridden expected row count.
- **CI VERIFIED:** quality test workflow PASS and separate official UCI-data workflow PASS.
- **NOT VERIFIED:** R execution, native Power BI PBIX/service deployment, accuracy of source descriptions beyond the provided fields, or live production retailer impact.

## Application disclosure

This is a new, independently built post-certificate portfolio project; it was not submitted to Coursera as an assessed project. Real UCI-derived findings are distinct from the synthetic demo. None of the figures belong to HOK-Elanto, VAKEHYVA, or any other employer.
