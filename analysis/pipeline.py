"""Auditable end-to-end retail analytics pipeline for the public UCI Online Retail dataset.

Business definitions are deliberately explicit: gross sales excludes cancellations,
returns are reported separately, and cancelled invoices are not automatically netted
against original sales because reliable matching references are unavailable.
"""
from __future__ import annotations

import argparse
import json
import sqlite3
from pathlib import Path

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

REQUIRED = ['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']


def load(path: str | Path) -> pd.DataFrame:
    path = Path(path)
    if path.suffix.lower() in ('.xlsx','.xls'):
        df = pd.read_excel(path, dtype={'InvoiceNo':str,'StockCode':str,'CustomerID':str})
    elif path.suffix.lower()=='.csv':
        df = pd.read_csv(path, dtype={'InvoiceNo':str,'StockCode':str,'CustomerID':str})
    else:
        raise ValueError('Expected .xlsx or .csv')
    missing = sorted(set(REQUIRED).difference(df.columns))
    if missing:
        raise ValueError('Missing columns: '+', '.join(missing))
    return df[REQUIRED].copy()


def clean(df:pd.DataFrame):
    """Retain clean sales, cancellations, and excluded rows separately."""
    raw = len(df)
    frame = df.copy()
    frame['InvoiceNo'] = frame['InvoiceNo'].astype('string').str.strip()
    frame['StockCode'] = frame['StockCode'].astype('string').str.strip()
    frame['Country'] = frame['Country'].astype('string').str.strip()
    frame['CustomerID'] = frame['CustomerID'].astype('string').str.replace(r'\.0$','',regex=True)
    frame['InvoiceDate'] = pd.to_datetime(frame['InvoiceDate'],errors='coerce')
    frame['Quantity'] = pd.to_numeric(frame['Quantity'],errors='coerce')
    frame['UnitPrice'] = pd.to_numeric(frame['UnitPrice'],errors='coerce')
    audit = {
        'raw_rows':raw,
        'exact_duplicate_rows':int(frame.duplicated().sum()),
        'missing_customer_id_rows':int(frame['CustomerID'].isna().sum()),
        'missing_description_rows':int(frame['Description'].isna().sum()),
        'invalid_dates':int(frame['InvoiceDate'].isna().sum()),
    }
    frame = frame.drop_duplicates()
    required_not_null = frame[['InvoiceNo','StockCode','InvoiceDate','Quantity','UnitPrice','Country']].notna().all(axis=1)
    valid = frame[required_not_null].copy()
    valid = valid[(valid['InvoiceNo'] != '') & (valid['Country'] != '') & (valid['UnitPrice'] >= 0)]
    cancel = valid['InvoiceNo'].str.upper().str.startswith('C',na=False)
    is_sale = (~cancel) & (valid['Quantity'] > 0) & (valid['UnitPrice'] > 0)
    is_return = cancel & (valid['Quantity'] < 0) & (valid['UnitPrice'] > 0)
    sales = valid[is_sale].copy()
    returns = valid[is_return].copy()
    other = valid[~(is_sale|is_return)].copy()
    sales['line_revenue_gbp'] = sales['Quantity'] * sales['UnitPrice']
    returns['return_value_gbp'] = -returns['Quantity'] * returns['UnitPrice']
    audit.update({
       'deduplicated_rows':len(frame),
       'valid_sale_rows':len(sales),
       'cancellation_rows':len(returns),
       'other_non_sale_rows':len(other),
       'dropped_invalid_rows':len(frame)-len(valid),
       'unknown_customer_sales_rows':int(sales['CustomerID'].isna().sum()),
    })
    assert len(sales)+len(returns)+len(other)==len(valid), 'classification must be exhaustive'
    return sales,returns,other,audit


def calculate(sales:pd.DataFrame,returns:pd.DataFrame):
    """Create independently interpretable KPIs, time series and ranked groupings."""
    if sales.empty:
        raise ValueError('No valid sales rows')
    revenue=float(sales['line_revenue_gbp'].sum())
    return_value=float(returns['return_value_gbp'].sum()) if len(returns) else 0.0
    invoices=int(sales['InvoiceNo'].nunique())
    monthly = (sales.assign(month=sales['InvoiceDate'].dt.to_period('M').astype(str))
               .groupby('month',as_index=False)['line_revenue_gbp'].sum())
    countries=(sales.groupby('Country',as_index=False)
               .agg(revenue_gbp=('line_revenue_gbp','sum'),orders=('InvoiceNo','nunique'))
               .sort_values('revenue_gbp',ascending=False))
    products=(sales.groupby(['StockCode','Description'],dropna=False,as_index=False)
              .agg(revenue_gbp=('line_revenue_gbp','sum'),units=('Quantity','sum'))
              .sort_values('revenue_gbp',ascending=False))
    # IMPORTANT: return value is separate, not claimed as a validated refund rate.
    kpis={
        'sale_lines':len(sales),
        'orders':invoices,
        'gross_sales_gbp':round(revenue,2),
        'cancellation_line_value_gbp':round(return_value,2),
        'average_order_value_gbp':round(revenue/invoices,2),
        'countries':int(sales['Country'].nunique()),
        'identified_customers':int(sales['CustomerID'].nunique(dropna=True)),
    }
    return kpis,monthly,countries,products


def sql_reconcile(sales:pd.DataFrame, kpis:dict):
    """Independently cross-check gross revenue and distinct orders with SQLite."""
    connection = sqlite3.connect(':memory:')
    try:
        sales[['InvoiceNo','Country','line_revenue_gbp']].to_sql('sales',connection,index=False)
        n_orders,gross=connection.execute('SELECT COUNT(DISTINCT InvoiceNo), SUM(line_revenue_gbp) FROM sales').fetchone()
    finally:
        connection.close()
    if n_orders!=kpis['orders'] or abs(gross-kpis['gross_sales_gbp'])>0.011:
        raise AssertionError('SQL/Pandas KPI reconciliation failed')
    return {'sql_distinct_orders':n_orders,'sql_gross_sales_gbp':round(gross,2),'matched':True}


def make_charts(monthly:pd.DataFrame,countries:pd.DataFrame,outdir:Path):
    chartdir=outdir/'charts'
    chartdir.mkdir(parents=True,exist_ok=True)
    fig,ax=plt.subplots(figsize=(10,5))
    ax.plot(monthly['month'].astype(str), monthly['line_revenue_gbp'].to_numpy()/1000,marker='o',linewidth=2)
    ax.set(title='Gross sales by month',xlabel='Invoice month',ylabel='Gross sales (£000)')
    ax.grid(axis='y',alpha=.25)
    ax.tick_params(axis='x',rotation=35)
    fig.tight_layout()
    fig.savefig(chartdir/'monthly_sales.png',dpi=155)
    plt.close(fig)
    fig,ax=plt.subplots(figsize=(10,5))
    top=countries.head(8).iloc[::-1]
    ax.barh(top['Country'].astype(str),top['revenue_gbp'].to_numpy()/1000)
    ax.set(title='Top markets by recorded gross sales',xlabel='Gross sales (£000)')
    fig.tight_layout()
    fig.savefig(chartdir/'country_sales.png',dpi=155)
    plt.close(fig)


def run(path:str|Path,outdir:str|Path):
    out=Path(outdir)
    out.mkdir(parents=True,exist_ok=True)
    source=load(path)
    sales,returns,other,audit=clean(source)
    kpis,monthly,countries,products=calculate(sales,returns)
    sqlcheck=sql_reconcile(sales,kpis)
    monthly.to_csv(out/'monthly_sales.csv',index=False)
    countries.to_csv(out/'country_sales.csv',index=False)
    products.head(20).to_csv(out/'top20_products.csv',index=False)
    result={'source':Path(path).name,'audit':audit,'kpis':kpis,'sql_check':sqlcheck,
            'data_limitations':['No cost-of-goods data: not a profit report',
                                'Cancellations are separate, cannot safely match all to source sales',
                                'CustomerID absent on some rows; customer counts exclude missing IDs',
                                'Historical UK non-store retailer; not representative of Finnish grocery shoppers']}
    (out/'quality_and_kpis.json').write_text(json.dumps(result,indent=2,ensure_ascii=False),encoding='utf-8')
    make_charts(monthly,countries,out)
    return result


if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',required=True)
    parser.add_argument('--out',default='output')
    args=parser.parse_args()
    print(json.dumps(run(args.input,args.out),indent=2,ensure_ascii=False))
