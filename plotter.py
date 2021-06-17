import matplotlib.pyplot as plt
plt.style.use('dark_background')
def actual(x, y):
    plt.plot(x, y)
    plt.grid(True)
    plt.show()

def overall(df):
    df.plot()
    plt.grid(True)
    plt.show()