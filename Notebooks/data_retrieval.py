from bs4 import BeautifulSoup
import requests
from urllib.parse import urljoin
from os.path import basename
import pandas as pd

base = "https://raw.githubusercontent.com/" 
url = requests.get('https://github.com/data-corentinv/tp_mlflow/blob/main/data/batchs/').text

soup = BeautifulSoup(url, features="html.parser")
#print([a["href"] for a in soup.find_all('a', href=lambda href: href and href.endswith('.csv'))])
all_urls = list(set((urljoin(base, a["href"]) for a in soup.find_all('a', href=lambda href: href and href.endswith('.csv')))))
all_csv = []
for link in all_urls:
    link2 = link.replace('/blob', '')
    print(link2)
    try :
        all_csv.append(pd.read_csv(link2))
        print('OK')
    except :
        print("KO")
        
base_finale = pd.concat(all_csv, axis=0)
base_finale.to_csv('base_finale.csv', index=False)
    