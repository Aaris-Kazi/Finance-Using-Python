import matplotlib.pyplot as plt
def actual(x, y):
    plt.grid(True)
    plt.plot(x, y)
    plt.show()

def overall(df):
    plt.grid(True)
    df.plot()
    plt.show()