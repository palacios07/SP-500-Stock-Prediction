# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 02:50:39 2020

@author: zhong
"""
###############################################################################
'load api data'

import alpha_vantage
from alpha_vantage.timeseries import TimeSeries

##########################################
import json
import time
from tqdm import tqdm
##################################
import sys, os
from pathlib import Path
project_dir = Path.cwd()
os.chdir(project_dir)
sys.path.append(os.getcwd())
#os.chdir('change to the mother working directory')

#_stock = json.loads(open('ticker_name_list.json').read())
_stock = json.loads(open('1-code to download, process, and present raw data/data/1-ticker_name_list.json').read())
tickers = list( _stock.keys() )

###############################################################################
#ts = TimeSeries(key='a api key free to download at https://www.alphavantage.co/')
#Here is your API key: AKWAHB33RHC5FNML
ts = TimeSeries(key='PZCDZH3NUNVLXZA2')

stock_data_AV = {}
#stock_data_AV  = json.loads(open('data\\stock_data_AV.json').read())

file_3_stock_log = open('1-code to download, process, and present raw data/data/3-stock-output.txt', 'w')


'load individual stock data for companies on list'
for stock in tqdm( tickers ):
    if stock not in stock_data_AV.keys():
        print("STOCK: " + stock)
        file_3_stock_log.write("\nSTOCK: " + stock)

        try:
            _data, _meta_data = ts.get_daily_adjusted(symbol = stock, outputsize = 'full') # added interval='1min'
            stock_data_AV[stock] = _data
            time.sleep(15)
        except:
            print(f"Error: {stock} not found in Alpha Vantage API")
            stock_data_AV[stock] = None


'save data'
with open('1-code to download, process, and present raw data/data/stock_data_AV.json', 'w') as fp:
    json.dump(stock_data_AV, fp)


file_3_stock_log.close()

