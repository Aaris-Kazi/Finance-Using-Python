import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

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
# print(stocks)
plt.plot(stocks['Date'], stocks['Volume'])
plt.show()