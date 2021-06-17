from finance_value import finance
import pandas as pd
import numpy as np
from plotter import *
from sklearn.linear_model import LinearRegression

def main():
    banner = "1: To load csv (GOOGLE)\n 2: Get Info \n 3: Graph of Stonks \n 3: Graph of Overall"
    print(banner)
    s = int(input('Select Value:'))
    if s == 1:
        finance()
    elif s == 2:
        df = pd.read_csv('google.csv')
        print(df.info())
    elif s == 3:
        df = pd.read_csv('google.csv')
        actual(df['Date'], df['Close'])
    elif s == 4:
        df = pd.read_csv('google.csv')
        overall(df)
    
if __name__ == "__main__":
    main()

