"""Download authoritative UCI Online Retail dataset locally, not into Git.

Dataset: Chen, D. (2015), CC BY 4.0, DOI: 10.24432/C5BW33.
The source URL is the official UCI data archive, not a copied tutorial.
"""
from pathlib import Path
from urllib.request import urlopen
from zipfile import ZipFile
import io

SOURCE_URL='https://archive.ics.uci.edu/static/public/352/online+retail.zip'


def download(destination=Path('data/raw')):
    destination=Path(destination)
    destination.mkdir(parents=True,exist_ok=True)
    with urlopen(SOURCE_URL,timeout=90) as response:
        archive=response.read()
    if len(archive)>100_000_000:
        raise ValueError('Unexpectedly large download; refusing to extract')
    with ZipFile(io.BytesIO(archive)) as zipfile:
        names=[n for n in zipfile.namelist() if n.lower().endswith('.xlsx') and '/' not in n.replace('\\','/')]
        if len(names)!=1:
            raise ValueError(f'Expected one xlsx in UCI archive; found {names}')
        data=zipfile.read(names[0])
    out=destination/'Online Retail.xlsx'
    out.write_bytes(data)
    print(f'Saved {len(data):,} bytes to {out}; do not commit data/raw/')


if __name__=='__main__':download()
