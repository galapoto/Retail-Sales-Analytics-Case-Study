import sys
import tempfile
import unittest
from pathlib import Path

import pandas as pd
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'analysis'))
from pipeline import load,clean,calculate,sql_reconcile,run


class RetailTests(unittest.TestCase):
    @staticmethod
    def example():
        rows=[
           ['1','A','ITEM',2,'2011-01-01',5,'100','Finland'],
           ['1','B','OTHER',1,'2011-01-01',10,'100','Finland'],
           ['1','B','OTHER',1,'2011-01-01',10,'100','Finland'], # exact duplicate
           ['C2','A','ITEM',-1,'2011-01-02',5,'100','Finland'],
           ['3','A','ITEM',2,'bad date',5,'101','Finland'],
           ['4','B','OTHER',0,'2011-01-02',10,None,'Sweden'],
           ['5','B','OTHER',2,'2011-01-03',0,None,'Sweden'],
        ]
        return pd.DataFrame(rows,columns=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country'])

    def test_classification_and_quality(self):
        sales,returns,other,audit=clean(self.example())
        self.assertEqual(audit['raw_rows'],7)
        self.assertEqual(audit['exact_duplicate_rows'],1)
        self.assertEqual(len(sales),2)
        self.assertEqual(len(returns),1)
        self.assertEqual(len(other),2)
        self.assertEqual(audit['dropped_invalid_rows'],1)

    def test_financial_metrics_not_net_returns(self):
        sales,returns,_,_=clean(self.example())
        kpis,*_=calculate(sales,returns)
        self.assertEqual(kpis['gross_sales_gbp'],20)
        self.assertEqual(kpis['cancellation_line_value_gbp'],5)
        self.assertEqual(kpis['orders'],1)
        self.assertEqual(kpis['average_order_value_gbp'],20)

    def test_sql_reconciles_pandas(self):
        sales,returns,_,_=clean(self.example())
        kpis,*_=calculate(sales,returns)
        self.assertTrue(sql_reconcile(sales,kpis)['matched'])

    def test_reject_invalid_schema(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'invalid.csv'
            path.write_text('bad,header\n1,2\n')
            with self.assertRaisesRegex(ValueError,'Missing columns'):
                load(path)

    def test_end_to_end_outputs(self):
        with tempfile.TemporaryDirectory() as td:
            path=Path(td)/'input.csv'
            self.example().to_csv(path,index=False)
            out=Path(td)/'out'
            report=run(path,out)
            self.assertTrue(report['sql_check']['matched'])
            for f in ['quality_and_kpis.json','monthly_sales.csv','country_sales.csv','top20_products.csv','charts/monthly_sales.png','charts/country_sales.png']:
                self.assertTrue((out/f).exists(), f)


if __name__=='__main__':unittest.main()
