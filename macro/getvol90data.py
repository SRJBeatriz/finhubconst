"""
Authors: Helena Bianchessi and Beatriz Jesus
"""
from bloomberg import BBG
import pandas as pd
from sklearn import preprocessing
import numpy as np
import matplotlib.pyplot as plt

bbg = BBG()

# Pulling IBOVESPA and S&P indexes volatility
#   Original Date: '28-fev-1967'

start_date = pd.to_datetime('30-jan-2015')
end_date = pd.to_datetime('today')

df = bbg.fetch_series(securities=['SPX Index', 'IBOV Index'],
                      fields=['VOLATILITY_90D'],
                      startdate=start_date,
                      enddate=end_date)

volSPX_90 = pd.DataFrame(data=df['SPX Index'])
volSPX_90 = volSPX_90.droplevel('FIELD')
volSPX_90 = volSPX_90.resample('Q').last()

volIBOV_90 = pd.DataFrame(data=df['IBOV Index'])
volIBOV_90 = volIBOV_90.droplevel('FIELD')
volIBOV_90 = volIBOV_90.resample('Q').last()

ax = plt.gca()

volSPX_90.plot(kind='line', color='blue', ax=ax)
volIBOV_90.plot(kind='line', color='green', ax=ax)

plt.show()

# Normalized series SPX

x = np.array(volSPX_90['SPX Index'])
spxnorm = preprocessing.normalize([x])
spxnorm = spxnorm.reshape(-1,1)

volnormSPX = volSPX_90
volnormSPX['SPX Index Normalized'] = ''
volnormSPX['SPX Index Normalized'] = spxnorm

# Normalized series IBOV

y = np.array(volIBOV_90['IBOV Index'])
ibovnorm = preprocessing.normalize([y])
ibovnorm = ibovnorm.reshape(-1,1)

volnormIBOV = volIBOV_90
volnormIBOV['IBOV Index Normalized'] = ''
volnormIBOV['IBOV Index Normalized'] = ibovnorm

# Info

volnormSPX.info()
volnormIBOV.info()
