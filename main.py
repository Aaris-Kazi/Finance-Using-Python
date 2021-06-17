from finance_value import finance
import pandas as pd
import numpy as np
from plotter import *
from sklearn.linear_model import LinearRegression

def main():
    # finance()
    df = pd.read_csv('google.csv')
    # print(df.info())
    # actual(df['Date'], df['Close'])
    overall(df)
    
if __name__ == "__main__":
    main()

