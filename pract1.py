import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
symbol = 'GOOGL'
ticker = yf.Ticker(symbol)
# print(ticker)
ticker_df = ticker.history(period= '1M', interval= '1D',start= '2021-05-15', end='2021-06-15')
# print(ticker_df['Volume'].shape)
days = pd.date_range(start= '2021-05-17', end='2021-06-05')
# print(days.shape)
# volume = ticker_df['Volume']
stocks = pd.DataFrame({
    "Date": days,
    "Volume": ticker_df['Volume']
})
days = []
for i in stocks['Date'].values:
    days.append(i)
days = np.array(days)
days.reshape(-1, 1)
print(days)
volume = []
for i in stocks['Volume']:
    volume.append(i)
volume = np.array(volume)
# volume.reshape(-1, 1)   
# print(days)
print(volume)
reg = LinearRegression().fit(volume, days)
print(LinearRegression.score())
LinearRegression(copy_X=True, fit_intercept=True, n_jobs=1, normalize=False)
# plt.grid(True)
# plt.plot(days, volume)
# plt.show()