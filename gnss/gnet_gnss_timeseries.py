
#%%
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.metrics import r2_score
import numpy as np
#%%
# import data
ds = pd.read_csv('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/DATASETS/GNET/KELY_NEU.csv')
# %%
#get correct data timeframe
df = ds.loc[6482:]
#df = ds
#add 
# fitting of subbed timeseries
x = np.arange(df['Time'].size) # = array([0, 1, 2, ..., 3598, 3599, 3600])
fit = np.polyfit(x, df['Up'], 1)
fit_fn = np.poly1d(fit)
model2 = np.poly1d(np.polyfit(x, df.Up, 2))
model3 = np.poly1d(np.polyfit(x, df.Up, 3))
model4 = np.poly1d(np.polyfit(x, df.Up, 4))
model5 = np.poly1d(np.polyfit(x, df.Up, 5))

reg_coeff = fit[0]
inters = fit[1]
print('Line eq = y = {} * x + {}'.format(reg_coeff, inters))

#r2_score(y, predict(x))

# timeseries
plt.plot(df['Time'], df['Up'], 'go', ms=2)
# linear
plt.plot(df['Time'], fit_fn(x), 'k-')
#2
#plt.plot(df['Time'], model2(x), 'b-')
#plt.plot(df['Time'], model3(x), 'b-')
#plt.plot(df['Time'], model4(x), 'b-')
#plt.plot(df['Time'], model5(x), 'b-')
# %%# plot full timeseires
plt.plot(ds['Time'], ds['Up'])
# %%
# fitting of full timeseries

