"""
Authors: Helena Bianchessi and Beatriz Jesus
"""
from bloomberg import BBG
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

bbg = BBG()

# Brazil FGV Consumer Confidence Index SA Sep 2005=100
#   Original Date: '30-sep-2005'

start_date = pd.to_datetime('01-jan-2010')
end_date = pd.to_datetime('15-jun-2019')

df = bbg.fetch_series(securities=['BZFGCCSA Index'],
                      fields=['PX_LAST'],
                      startdate=start_date,
                      enddate=end_date)

consbr = pd.DataFrame(data=df)
consbr = consbr.droplevel(0)
consbr = consbr.reset_index()
consbr = consbr.set_index('TRADE_DATE')
consbr = consbr.resample('Q').mean()

# Normalized series Consumer Confidence

x = np.array(consbr['BZFGCCSA Index'])
x = x.reshape(-1,1)

min_max_scaler = preprocessing.MinMaxScaler()
x_scaled = min_max_scaler.fit_transform(x)

confnorm = concconf
confnorm['CONCCONF Normalized'] = ''
confnorm['CONCCONF Normalized'] = x_scaled
confnorm = confnorm.drop('CONCCONF Index', axis=1)

#confnorm.info()
#print(confnorm)

ax = plt.gca()
confnorm.plot(kind='line', y='CONCCONF Normalized', color='green', ax=ax)
plt.show()