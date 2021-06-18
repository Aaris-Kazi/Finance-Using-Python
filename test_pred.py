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
dummy_dates = []

for i in range(len(df['Date'])):
    dummy_dates.append(i)
dummy_dates = np.array(dummy_dates).reshape(-1, 1)
# print(dummy_dates)
close = df['Close'].values
close = close.reshape(-1, 1); close
# print(close)

# dt.pred = pd.to_datetime(dt.pred)
# print(dt.pred.values.astype(float).reshape(-1, 1))
# print(a.values.astype(float))
# reg = LinearRegression().fit(close, days)
# b = reg.predict(dt.pred.values.astype(float).reshape(-1, 1))
# print('%4f'%float(b))

reg = LinearRegression().fit(dummy_dates, close)
a = np.array([[22],[23],[24],[25],[26]])
print(a)
b = reg.predict(a)
print(b)
plt.plot(dummy_dates, close)
plt.scatter(a,b)
plt.legend(['Actual', 'Predicted'])
plt.show()