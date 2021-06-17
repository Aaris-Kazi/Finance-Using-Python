from finance_value import finance
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# finance()
df = pd.read_csv('google.csv')
print(df.info())
plt.grid(True)
plt.plot(df['Date'], df['Volume'])
plt.show()