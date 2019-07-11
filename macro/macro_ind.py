from bloomberg import BBG
import pandas as pd
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

volIBOV_90 = pd.DataFrame(data=df['IBOV Index'])
volIBOV_90 = volIBOV_90.droplevel('FIELD')


print(volSPX_90)
print(volIBOV_90)

# Conference Board Consumer Confidence SA 1985=100
#   Original Date: '28-fev-1967'

start_date = pd.to_datetime('30-jan-2015')
end_date = pd.to_datetime('30-jun-2019')

df = bbg.fetch_series(securities=['CONCCONF Index'],
                      fields=['PX_LAST'],
                      startdate=start_date,
                      enddate=end_date)

concconf = pd.DataFrame(data=df)
concconf = concconf.droplevel(0)
concconf = concconf.resample('Q').mean()

print(concconf)
