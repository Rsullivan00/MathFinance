import pandas as pd
from pandas.io.data import DataReader
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt

ibm = DataReader("IBM",  "yahoo", datetime(2009,1,1), datetime(2014,12,31))
print ibm.head()
stkp = ibm["Adj Close"]
daily_returns = np.subtract(stkp[1:], stkp[:-1])
annual_stkp = ibm.resample('A')['Adj Close']
annual_returns = np.subtract(annual_stkp[1:], annual_stkp[:-1])
print daily_returns 
print annual_returns 
# a
print 'Mean daily return: %s' % daily_returns.mean()
print 'Mean annual return: %s' % annual_returns.mean()

# b
print 'Daily standard deviation: %s' % daily_returns.std()
print 'Annual standard deviation: %s' % annual_returns.std()

# c
print 'Histogram of returns for 1 year:\n%s' % daily_returns[:260].value_counts()
df = pd.DataFrame(daily_returns[:260])
plt.figure()
df.hist()
plt.show()

# d
print 'Histogram of returns for whole horizon:\n%s' % daily_returns.value_counts()
df = pd.DataFrame(daily_returns)
plt.figure()
df.hist()
plt.show()

# e

# f

# g
