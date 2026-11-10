# Data handling and integrity

- Actual data source: Daqing Chen (2015), UCI Online Retail, CC BY 4.0, DOI 10.24432/C5BW33. **Not included in the repo.**
- Run `python scripts/download_uci.py` to fetch the official ZIP and save extracted `Online Retail.xlsx` locally into the ignored `data/raw/` directory.
- Run `python scripts/make_demo.py` for a deterministic **synthetic** demonstration (seed 42). The generated CSV is also ignored and can be recreated.
- Do not substitute synthetic metrics for source dataset findings.
- Do not commit customer records, credentials or other sensitive private data.
