import yfinance as yf
import pandas as pd
import streamlit as st

st.write('# Can be used in Website')
symbol = 'GOOGL'
ticker = yf.Ticker(symbol)
ticker_df = ticker.history(period= '1M', interval= '1D',start= '2021-05-15', end='2021-06-15')
x = ticker_df.Close
y = ticker_df.Volume
st.line_chart(x)
st.line_chart(y)