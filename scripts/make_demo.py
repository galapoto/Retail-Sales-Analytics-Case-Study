"""Deterministic synthetic fixture only: NEVER label outputs as real UCI results."""
from pathlib import Path
import numpy as np
import pandas as pd


def make_fixture(path:Path, n_orders=2000, seed=42):
    rng=np.random.default_rng(seed)
    products=[('P001','TEA MUG',3.5),('P002','BLUE CANDLE',5.1),('P003','DESK NOTEBOOK',7.2),
              ('P004','WOODEN FRAME',12.5),('P005','COTTON BAG',6.75),('P006','STORAGE JAR',9.4)]
    countries=['United Kingdom','Germany','France','EIRE','Finland']
    probs=[.70,.12,.08,.07,.03]
    rows=[]
    for i in range(n_orders):
        month=int(rng.integers(1,13))
        day=int(rng.integers(1,29))
        date=f'2011-{month:02d}-{day:02d} 12:00:00'
        customer=str(12000 + i%300) if rng.random()>.03 else None
        country=str(rng.choice(countries,p=probs))
        for _ in range(int(rng.integers(1,5))):
            stock,descr,price=products[int(rng.integers(0,len(products)))]
            rows.append([str(500000+i),stock,descr,int(rng.integers(1,9)),date,price,customer,country])
        if rng.random()<.08:
            stock,descr,price=products[int(rng.integers(0,len(products)))]
            rows.append([f'C{500000+i}',stock,descr,-int(rng.integers(1,4)),date,price,customer,country])
    if rows:rows.append(rows[0])  # deliberate duplicate for quality-audit test
    path.parent.mkdir(parents=True,exist_ok=True)
    pd.DataFrame(rows,columns=['InvoiceNo','StockCode','Description','Quantity','InvoiceDate','UnitPrice','CustomerID','Country']).to_csv(path,index=False)
    return len(rows)

if __name__=='__main__':
    path=Path('data/synthetic_retail_demo.csv')
    print('Synthetic fixture rows:',make_fixture(path))
