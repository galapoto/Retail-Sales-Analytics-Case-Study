# Reproducing and interpreting the retail analysis

## Independent official-source verification

The public GitHub workflow downloaded the original UCI Excel, processed **541,909 source records**, reconciled gross sales and distinct invoices against SQLite, and published results at [results/uci](../results/uci/README.md) on 10 November 2026.

The downloaded Excel SHA-256 is `43465a06f2ccf7c8b5bd2892bc7defb52f97487934fe93b16ae4c3936424676d`. The verified workflow run is [42759973718](https://github.com/galapoto/Retail-Sales-Analytics-Case-Study/actions/runs/42759973718).

## Local instructions

1. Create and activate a Python virtual environment.
2. Run: pip install -r requirements.txt.
3. Run: python scripts/download_uci.py.
4. Run: python analysis/pipeline.py --input "data/raw/Online Retail.xlsx" --out output/uci.
5. Run: python -m unittest discover -s tests -v.
6. Inspect the audit JSON, country/month/product exports and charts from output/uci.

Alternatively, use the GitHub Actions workflow "Analyze official UCI Online Retail source" to regenerate the aggregate reports, including source checksum and a row-count gate.

## Offline fixture (synthetic, not UCI)

Run python scripts/make_demo.py, then python analysis/pipeline.py --input data/synthetic_retail_demo.csv --out output/demo. These examples test the pipeline but are not real retail findings.

## Quality and scope limits

- Schema checks and source row-count gate prevent silent source-file substitution.
- Missing customer IDs, exact duplicates, invalid dates, cancellations and non-sale lines are audited separately.
- Positive non-cancelled sale lines are summed for gross sales; cancellation values are kept distinct, not silently subtracted.
- SQLite independently checks the order count and revenue calculation.
- This dataset is UK non-store retail from 2010–2011; it cannot prove modern Nordic demand, profit or causal commercial effects.
- R code and the Power BI modelling blueprint are included, but no independently executed R verification or deployed Power BI .pbix is claimed.
