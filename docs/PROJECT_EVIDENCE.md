# Build provenance and verification

**Status updated:** 10 November 2026.

## Implementation scope

- NEW analysis/pipeline.py: input validation, classification, quality audit, KPI calculations, Pandas/SQLite cross-check and chart/CSV exports.
- NEW scripts/make_demo.py: deterministic synthetic generator with intentional duplicate source rows.
- NEW scripts/download_uci.py: UCI archive downloader, intentionally saving source data outside version control.
- NEW tests/test_pipeline.py: five automated tests including end-to-end generation and SQL/Pandas reconciliation.
- NEW analysis/retail_case_study.R: optional R verification; execution has not been verified.
- NEW analysis/sql_checks.sql: example manual SQL checks.
- NEW dashboard/POWER_BI_MODEL.md: measure/schema guidance; a PBIX is not included.
- NEW preview/retail_demo_dashboard.svg: recruiter preview generated from synthetic fixture output, not official source findings.

## Source/reuse provenance

**COPIED: none.** The target GitHub repository was initially empty. No third-party project source code was imported. The original pipeline was written as a self-contained portfolio case study.

**ADAPTED:** Google Data Analytics capstone process (Ask, Prepare, Process, Analyze, Share, Act), with newly written Python/SQL/R implementations.

**EXTERNAL DATA REFERENCE:** Daqing Chen (2015), UCI Online Retail, CC BY 4.0, DOI 10.24432/C5BW33. No raw source data or Coursera proprietary starter datasets are committed.

**INTEGRATED:** GitHub Actions runs unit tests and regenerates synthetic reports for verification.

## Verification status

- Python unit tests: **5/5 PASS locally** on 10 November 2026.
- GitHub Actions: check the repository's Actions tab for the actual result of this commit; do not treat a workflow file alone as a passing check.
- Full historical 541,909-row UCI run: **NOT VERIFIED**.
- Native Power BI dashboard: **NOT IMPLEMENTED**.
- Optional R execution: **NOT VERIFIED**.
- Original Coursera capstone submission: **NOT CLAIMED**. This is a new independent portfolio project developed after the certificate.

## Integrity rule

The example visual and small demo numbers are **synthetic**. Never present them as actual commercial findings, a HOK-Elanto dataset, a production report or independently validated source-specific conclusions.
