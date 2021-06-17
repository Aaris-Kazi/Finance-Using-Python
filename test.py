import datetime
import pandas as pd
import pandas_datareader.data as web
print(datetime.date.today())
df = web.DataReader('TSLA', 'yahoo', '2021-05-15', datetime.date.today())
df.to_csv('TSLA.csv')