import numpy as np
import pandas as pd
import pandas_datareader.data as web
import datetime
import t_demo as ts
# e = ts.get_hist_data('000725',start='2020-06-23',end='2020-06-26')
# print(e.head())

# df_csvsave = web.DataReader("000725.SZ", "yahoo", datetime.datetime(2020, 1, 1), datetime.date.today())
# print(df_csvsave.head())

pro = ts.pro_api()

#查询当前所有正常上市交易的股票列表

# data = pro.stock_basic(exchange='', list_status='L', fields='ts_code,symbol,name,area,industry,list_date')
# print(data)