import yfinance as yf
import datetime
import pandas_datareader.data as web
# print(datetime.date.today())
def finance():
    symbol = 'GOOGL'
    ticker = yf.Ticker(symbol)
    # print(ticker)
    ticker_df = ticker.history(period= '1M', interval= '1D',start= '2021-05-15', end=datetime.date.today())
    ticker_df.to_csv('google.csv')
    print('CSV has been initialised!')
    

def bypd():
    df = web.DataReader('TSLA', 'yahoo', '2021-05-15', datetime.date.today())
    df.to_csv('TSLA.csv')