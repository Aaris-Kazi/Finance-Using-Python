from finance_value import finance
import pandas as pd
import numpy as np
from plotter import actual
from sklearn.linear_model import LinearRegression

# finance()
df = pd.read_csv('google.csv')
# print(df.info())
actual(df['Date'], df['Volume'])
