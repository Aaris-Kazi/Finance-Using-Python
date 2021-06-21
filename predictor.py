import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import svm
from plotter import chart_predict

def forlinear():
    
    df = pd.read_csv('google.csv')
    df.Date= pd.to_datetime(df.Date)
    days = df['Date'].values
    days = days.reshape(-1, 1); days
    dummy_dates = []

    for i in range(len(df['Date'])):
        dummy_dates.append(i)
    dummy_dates = np.array(dummy_dates).reshape(-1, 1)
    # print(dummy_dates)
    close = df['Close'].values
    close = close.reshape(-1, 1); close
    # print(close)

    # dt.pred = pd.to_datetime(dt.pred)
    # print(dt.pred.values.astype(float).reshape(-1, 1))
    # print(a.values.astype(float))
    # reg = LinearRegression().fit(close, days)
    # b = reg.predict(dt.pred.values.astype(float).reshape(-1, 1))
    # print('%4f'%float(b))

    reg = LinearRegression().fit(dummy_dates, close)
    a = np.array([[22],[23],[24],[25],[26]])
    # print(a)
    b = reg.predict(a)
    # print(b)
    # plt.plot(dummy_dates, close)
    # plt.scatter(a,b)
    # plt.legend(['Actual', 'Predicted'])
    # plt.show()
    chart_predict(dummy_dates, close, a, b)
def forsvm():
    df = pd.read_csv('google.csv')
    dummy_dates = []
    for i in range(len(df['Date'])):
        dummy_dates.append(i)
    dummy_dates = np.array(dummy_dates).reshape(-1, 1)
    print(dummy_dates)
    close = df['Close'].values
    print(close)
    # x = [[0, 0], [1, 1]]
    # y = [0, 1]
    # close = close.reshape(-1, 1); close
    
    clf = svm.SVC(decision_function_shape= 'ovo') # 7
    # clf = svm.NuSVC() # 7
    # clf = svm.LinearSVC() # 7
    clf.fit(dummy_dates, close)
    # a = np.array([[22],[23],[24],[25],[26]])
    # b = clf.predict(a)
    # print(b)
    # chart_predict(dummy_dates, close, a, b)
