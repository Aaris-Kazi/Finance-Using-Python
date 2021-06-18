import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
def actual(x, y):
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

def overall(df):
    df.plot()
    plt.grid(True)
    plt.show()

def chart_predict(x, y, a, b):
    plt.plot(x, y)
    plt.scatter(a, b)
    plt.grid(True)
    plt.legend(['Actual', 'Predicted'])
    plt.show()