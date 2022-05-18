import pandas as pd
import numpy as np

s = pd.Series([1, 3, 5, np.nan, 6, 8])
# print(s)

dates = pd.date_range("2020-01-01", periods=10)
# print(dates)

column = list('ABCD')
index = dates
contents = np.random.randn(10, 4)
# print(contents)
# print(column)
# print(index)

df = pd.DataFrame(contents, index=index, columns=column)
# print(df)

dfN = df.to_numpy()
# print(dfN)

dfD = df.describe()
# print(dfD)

print(df[0:3])
