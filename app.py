import requests
import pandas as pd
import numpy as np
import json
from bs4 import BeautifulSoup

# class YieldWatcher:
#     def __init__(self, mode='default'):
#         self.sources = []
#         self.min_liq = 1000000000
        
#     def get_current_rates(self,)


bin_earn = requests.get('https://www.binance.com/bapi/earn/v1/friendly/defi-pos/groupByAssetAndPartnerNameList?pageIndex=1&status=ALL').json()
bin_locked_staking = requests.get('https://www.binance.com/bapi/earn/v1/friendly/pos/union?pageIndex=1&status=SUBSCRIBABLE').json()

# print(pd.DataFrame(bin_earn['data']))
# print(pd.DataFrame(bin_locked_staking['data']))

# def all_bin_lsk():
#     url = 'https://www.binance.com/bapi/earn/v1/friendly/defi-pos/groupByAssetAndPartnerNameList?'
t = requests.get('https://www.binance.com/bapi/earn/v1/friendly/pos/union').json()
total = t['total']
print(total)
loops = int(np.ceil(total/15))
print(loops)
adata = []
projects = []
for i in range(loops):
    ix = i+1
    print(i)
    res = requests.get(f'https://www.binance.com/bapi/earn/v1/friendly/pos/union?pageSize=15&pageIndex={ix}&status=SUBSCRIBABLE').json()
    for i in res['data']:
        adata.append(i)
        projects.append(i['projects'])
    
print(pd.DataFrame(projects[15]))
print(pd.DataFrame(adata))