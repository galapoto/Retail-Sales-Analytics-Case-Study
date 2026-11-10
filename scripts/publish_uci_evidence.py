"""Publish source-validated aggregate reports without the raw dataset."""
import argparse
import hashlib
import json
import shutil
from datetime import datetime, timezone
from pathlib import Path

CITATION = 'Chen, D. (2015), Online Retail, UCI, CC BY 4.0, DOI 10.24432/C5BW33'


def publish(outdir: Path, raw_file: Path, destination: Path, expected_rows: int):
    outdir, raw_file, destination = map(Path, (outdir, raw_file, destination))
    report = json.loads((outdir / 'quality_and_kpis.json').read_text(encoding='utf-8'))
    observed = report['audit']['raw_rows']
    if observed != expected_rows:
        raise ValueError(f'Raw row count mismatch: observed={observed}, expected={expected_rows}')
    if not report['sql_check']['matched']:
        raise ValueError('SQL/Pandas reconciliation did not pass')
    if not raw_file.is_file():
        raise FileNotFoundError(raw_file)
    destination.mkdir(parents=True, exist_ok=True)
    for filename in ('quality_and_kpis.json', 'monthly_sales.csv', 'country_sales.csv', 'top20_products.csv'):
        shutil.copyfile(outdir / filename, destination / filename)
    (destination / 'charts').mkdir(exist_ok=True)
    for name in ('monthly_sales.png', 'country_sales.png'):
        shutil.copyfile(outdir / 'charts' / name, destination / 'charts' / name)
    with raw_file.open('rb') as handle:
        digest = hashlib.file_digest(handle, 'sha256').hexdigest()
    meta = {
        'source': CITATION,
        'source_url': 'https://archive.ics.uci.edu/dataset/352/online+retail',
        'source_file_sha256': digest,
        'observed_raw_rows': observed,
        'sql_reconciled': True,
        'utc_generated_at': datetime.now(timezone.utc).isoformat(),
        'notes': 'Aggregate derived indicators only; original source file excluded.',
    }
    (destination / 'source_provenance.json').write_text(json.dumps(meta, indent=2), encoding='utf-8')
    k, a = report['kpis'], report['audit']
    summary = f'''# Real UCI Online Retail — validated descriptive analysis

**Data source:** {CITATION}. Historical UK non-store retailer, 2010–2011.
**Source SHA-256:** {digest}. **Original rows:** {observed:,}. **SQL/Pandas check:** PASS.

| Measure | Observed value | Definition |
|---|---:|---|
| Gross sales | £{k['gross_sales_gbp']:,.2f} | Positive non-cancelled sale lines before returns and costs |
| Distinct sale invoices | {k['orders']:,} | Invoice-based order count |
| Average order value | £{k['average_order_value_gbp']:,.2f} | Gross sales / orders |
| Cancellation line value | £{k['cancellation_line_value_gbp']:,.2f} | Separately reported; not netted |
| Valid sale lines | {a['valid_sale_rows']:,} | Post-cleaning sales |
| Exact duplicate rows | {a['exact_duplicate_rows']:,} | Excluded before metrics |
| Rows missing CustomerID | {a['missing_customer_id_rows']:,} | Not assumed to be unique persons |
| Distinct sales markets | {k['countries']} | Country values in sale lines |

![Monthly sales](charts/monthly_sales.png)

![Gross sales by country](charts/country_sales.png)

**Limitations:** Historical descriptive analysis only. Profit, causality, current Finnish retail
performance and 2026 market conditions are not established. No row-level identifiers are published.
'''
    (destination / 'README.md').write_text(summary, encoding='utf-8')
    return meta


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--outdir', required=True, type=Path)
    parser.add_argument('--raw-file', required=True, type=Path)
    parser.add_argument('--destination', required=True, type=Path)
    parser.add_argument('--expected-rows', required=True, type=int)
    args = parser.parse_args()
    print(json.dumps(publish(args.outdir, args.raw_file, args.destination, args.expected_rows), indent=2))
