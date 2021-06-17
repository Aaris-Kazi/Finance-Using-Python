import yfinance as yf
import datetime

# print(datetime.date.today())
def finance():
    symbol = 'GOOGL'
    ticker = yf.Ticker(symbol)
    # print(ticker)
    ticker_df = ticker.history(period= '1M', interval= '1D',start= '2021-05-15', end=datetime.date.today())
    return ticker_df