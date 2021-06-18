import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

style.use('fivethirtyeight')
df = pd.read_csv('google.csv')
df.Date= pd.to_datetime(df.Date)
days = df['Date'].values
days = days.reshape(-1, 1); days

close = df['Close'].values
close = close.reshape(-1, 1); close
a = np.asarray(['2021-06-19'])
dt = pd.DataFrame({
    "pred": a
})

dt.pred = pd.to_datetime(dt.pred)
print(dt.pred.values.astype(float).reshape(-1, 1))
# print(a.values.astype(float))
reg = LinearRegression().fit(close, days)
b = reg.predict(dt.pred.values.astype(float).reshape(-1, 1))
print('%4f'%float(b))
plt.plot(days, close)
# plt.scatter(a,b)
plt.show()