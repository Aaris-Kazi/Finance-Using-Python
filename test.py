import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from sklearn import linear_model

data_time = np.asarray(['2017-05-24', '2017-05-25', '2017-05-26',
                        '2017-05-27', '2017-05-28', '2017-05-29',
                        '2017-05-30', '2017-05-31', '2017-06-01',
                        '2017-06-02', '2017-06-03', '2017-06-04',
                        '2017-06-05', '2017-06-06', '2017-06-07',
                        '2017-06-08', '2017-06-09', '2017-06-10',
                        '2017-06-11', '2017-06-12', '2017-06-13',
                        '2017-06-14', '2017-06-15', '2017-06-16',
                        '2017-06-17', '2017-06-18', '2017-06-19',
                        '2017-06-20', '2017-06-21'])
data_count = np.asarray([300.000, 301.000, 302.000, 303.000, 304.000,
                         305.000, 306.000, 307.000, 308.000, 309.000,
                         310.000, 311.000, 312.000, 230.367, 269.032,
                         258.867, 221.645, 222.323, 212.357, 198.516,
                         230.133, 243.903, 244.320, 207.451, 192.710,
                         212.033, 216.677, 222.333, 208.710])

df = pd.DataFrame({'time': data_time, 'count': data_count})
df.time = pd.to_datetime(df.time)

regr = linear_model.LinearRegression()
time = df.time.values
time = time.reshape(-1, 1); time
print(time)
count =df['count'].values
count = count.reshape(-1, 1); count
regr.fit(time, count)

# Make predictions using the testing set
y_pred = regr.predict(df.time.values.astype(float).reshape(-1, 1))
df['pred'] = y_pred

ax = df.plot(x='time', y='count', color='black', style='.')
df.plot(x='time', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)
ax.set_title('My Title')
ax.set_xlabel('Date')
ax.set_ylabel('Metric')

plt.show()