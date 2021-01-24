import sys

import numpy as np
import pandas as pd

df = pd.DataFrame({
    'A': ['foo', 'bar', 'foo', 'bar', 'foo', 'bar', 'foo', 'foo'],
    'B': ['one', 'one', 'two', 'three', 'two', 'two', 'one', 'three'],
    'C': np.random.randn(8),
    'D': np.random.randn(8)
})
print(df)
print(df.groupby('C').agg([np.sum, np.mean, np.std]))
# n = pd.pivot_table(df, values='D', index=['A', 'B'], columns=['C'])
# print(n)