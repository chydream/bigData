import numpy as np
import pandas as pd
import tushare as ts
pro = ts.pro_api('399a0d4366d4c410229527c175b068ba986b442736c920b99d83db4a')
data = pro.stock_basic(is_hs='', list_status='L', exchange='', fields='ts_code,symbol,name,area,industry,list_date')
print(type(data))
data.to_csv('test.csv')