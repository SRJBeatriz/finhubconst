"""
Authors: Helena Bianchessi and Beatriz Jesus
"""
from bloomberg import BBG
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

bbg = BBG()
min_max_scaler = preprocessing.MinMaxScaler()

# Pulling US Generic Govt 10 Year Yield volatility
#   Original Date: '01-feb-1962'

start_date = pd.to_datetime('01-jan-2010')
end_date = pd.to_datetime('16-jul-2018')

df = bbg.fetch_series(securities=['USGG10YR Index'],
                      fields=['Volatil 90D'],
                      startdate=start_date,
                      enddate=end_date)

volbonds_90 = pd.DataFrame(data=df['USGG10YR Index'])
volbonds_90 = volbonds_90.droplevel('FIELD')
volbonds_90 = volbonds_90.resample('Q').last()

#ax = plt.gca()
#volbonds_90.plot(kind='line', color='blue', ax=ax)
#plt.show()

# Normalized series

x = np.array(volbonds_90['USGG10YR Index'])
x = x.reshape(-1,1)
bondsnorm = min_max_scaler.fit_transform(x)

volnormbonds = volbonds_90
volnormbonds['Bonds Vol. Normalized'] = ''
volnormbonds['Bonds Vol. Normalized'] = bondsnorm
volnormbonds = volnormbonds.drop('USGG10YR Index', axis=1)

# Info
volnormbonds.info()

# Plotting

ax = plt.gca()
volnormbonds.plot(kind='line', color='green', ax=ax)
plt.show()
