import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import matplotlib.animation as animated
import time
style.use('fivethirtyeight')

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
def update(i):
    xs = []
    ys = []
    df = pd.read_csv('test.csv')
    n = len(df['Close'])
    for i in range(n):
        xs.append(df.Date[i])
        ys.append(df.Close[i])
        
    ax.clear()
    ax.plot(xs, ys)

ani = animated.FuncAnimation(fig, update, frames= 3,interval =2)
plt.show()