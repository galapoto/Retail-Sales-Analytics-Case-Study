# Reproducibility, risks and limitations

## Run on the actual public dataset

1. Create a virtual environment and install requirements: pip install -r requirements.txt.
2. Run python scripts/download_uci.py to download the official UCI ZIP and extract Online Retail.xlsx into the ignored data/raw/ folder.
3. Run python analysis/pipeline.py --input "data/raw/Online Retail.xlsx" --out output/uci.
4. Run python -m unittest discover -s tests -v.
5. Inspect output/uci/quality_and_kpis.json, monthly_sales.csv, country_sales.csv, top20_products.csv and the charts/ folder.

The real-data run is **NOT VERIFIED** at the time of publication because the source archive was unavailable in the preparation environment. Do not cite synthetic metrics as official UCI findings.

## Offline synthetic demonstration

1. Run python scripts/make_demo.py.
2. Run python analysis/pipeline.py --input data/synthetic_retail_demo.csv --out output/demo.
3. Optionally run python scripts/make_preview.py to regenerate the synthetic PNG preview locally.

The generator is deterministic (seed 42) and produces intentionally duplicated rows for auditing. The generated CSV is excluded from Git; the source generator is committed.

## Verification gates

- Rejects unexpected source schemas.
- Tracks exact duplicates, missing descriptions/customer IDs and invalid timestamps.
- Classifies positive sales and invoice cancellations separately.
- Reconciles gross sales and distinct invoices with independent in-memory SQLite queries.
- Saves full audit/metrics JSON and CSV/PNG artifacts in a single pipeline command.
- Five automated regression tests run on a small synthetic fixture.

## Limitations

- **Historic and non-local:** the 2010–2011 UK non-store retailer data cannot establish current Finnish grocery behavior.
- **Cancellation matching:** cancelled lines cannot be reliably matched to original invoices without documented keys.
- **Profit:** no acquisition costs, margins, operating costs or cost-of-goods figures.
- **Customer analytics:** missing CustomerID means some behavior is unidentifiable.
- **Statistical inference:** descriptive trends are not causal explanations.
- **Microsoft Power BI:** the DAX schema is a blueprint; a native .pbix and live Power BI Service report are not included.
