import sys

import numpy as np
import pandas as pd

np.set_printoptions(threshold=sys.maxsize)
s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s[0])
dates = pd.date_range('20200101', periods=6)
# print(dates)
# print(type(dates))
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print(df)
# a = np.random.randn(6, 4)
# print(type(a))
df2 = pd.DataFrame({
    'A': 1.,
    'B': pd.Timestamp('20130102'),
    'C': pd.Series(1, index=list(range(4)),dtype='float32'),
    'D': np.array([3]*4, dtype='int32'),
    'E': pd.Categorical(['test', 'train', 'test', 'train']),
    'F': 'foo'
})
# print(df2.head())
# print(df2.tail())
# print(df2.index)
# print(df2.columns)
# print(df2.to_numpy())
# print(df2.describe())
# print(df2.T)
# print(df2.sort_index(axis=0, ascending=True))
# print(df2.sort_values(by='E'))
# print(df2['B'])
# print(df2[0:3])

obj = pd.Series([40, 12, -3, 25], index=['a', 'b', 'c', 'd'])
# print(obj)
# print(obj.describe())
# print(obj.to_dict())
d = {'one': pd.Series([1., 2., 3.], index=['a', 'b', 'c']), 'two': pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
# print(df)
data = pd.read_csv('test.csv')
# print(data.head())
# data.to_excel('new.xls')
# print(data.describe())
# print(data.info())
# print(data.sort_values(by=['ts_code'], ascending=[False]))
# print(data.rename(columns={'Unnamed: 0 ': 'id'}))
# print(data.loc[:, ['ts_code', 'industry', 'name']])
# print(data.iloc[:4, [1,4]])
# print(data._ix[:4, ['ts_code', 'name']])
# print(data)
# print(data[data['industry'] == '银行'])
industry = data['industry']
# print(data['industry'])
# print(type(industry))
# print(dir(industry))
# print(industry.describe())
# print(industry.rank())
# cat = pd.cut(data.industry, bins=['银行', '软件服务'])
# print(data.groupby(industry).count())
