from bloomberg import BBG
import pandas as pd
import scipy
import matplotlib.pyplot as plt

bbg = BBG()

# IBOVESPA and S&P indexes volatility
#   Original Date: '28-fev-1967'

start_date = pd.to_datetime('30-jan-2015')
end_date = pd.to_datetime('today')

df = bbg.fetch_series(securities=['SPX Index', 'IBOV Index'],
                      fields=['VOLATILITY_90D'],
                      startdate=start_date,
                      enddate=end_date)

volSPX_90 = pd.DataFrame(data=df['SPX Index'])
volSPX_90 = volSPX_90.droplevel('FIELD')
volSPX_90 = volSPX_90.resample('Q').mean()

volIBOV_90 = pd.DataFrame(data=df['IBOV Index'])
volIBOV_90 = volIBOV_90.droplevel('FIELD')
volIBOV_90 = volIBOV_90.resample('Q').mean()

ax = plt.gca()

volSPX_90.plot(kind='line', color='blue', ax=ax)
volIBOV_90.plot(kind='line', color='green', ax=ax)

plt.show()