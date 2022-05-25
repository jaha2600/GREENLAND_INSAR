
#%%
import pandas as pd
import matplotlib.pyplot as plt
#from sklearn.metrics import r2_score
import numpy as np
import os
from mintpy.utils import utils as ut, plot as pp
#%%
# import data
ds = pd.read_csv('/data/GREENLAND/2022/GNET_TIMESERIES/KELY_NEU.csv')
# %%
#get correct data timeframe
df = ds.loc[6482:]
# fitting of subset timeseries
x = np.arange(ds['Time'].size) # = array([0, 1, 2, ..., 3598, 3599, 3600])
fit = np.polyfit(x, ds['Up'], 1)
fit_fn = np.poly1d(fit)
model2 = np.poly1d(np.polyfit(x, ds.Up, 2))
model3 = np.poly1d(np.polyfit(x, ds.Up, 3))
model4 = np.poly1d(np.polyfit(x, ds.Up, 4))
model5 = np.poly1d(np.polyfit(x, ds.Up, 5))

fit_2 = np.poly1d(model2)
fit_3 = np.poly1d(model3)
reg_coeff = fit_3[0]
inters = fit_3[1]
print('Line eq = y = {} * x + {}'.format(reg_coeff, inters))

#r2_score(y, predict(x))

# timeseries
plt.plot(ds['Time'], ds['Up'], 'go', ms=2)
# linear
plt.plot(ds['Time'], fit_3(x), 'k--')
#plt.plot(df['Time'], model2(x), 'b-')
#plt.plot(df['Time'], model3(x), 'b-')
#plt.plot(df['Time'], model4(x), 'b-')
#plt.plot(df['Time'], model5(x), 'b-')
# %% plot full timeseires
plt.plot(ds['Time'], ds['Up'], 'go', ms=2)
# %%
# plotting of full timeseries similar to mintpy style
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[6, 3])
ax.scatter(ds['Time'], ds['Up'], marker='o', s=2, facecolors='none', edgecolors='g', linewidth=1.)
ax.plot(ds['Time'], fit_3(x), 'k--')
ax.plot(ds['Time'], fit_fn(x), 'r--')
# axis format edited for ylim values. 
ax.tick_params(which='both', direction='in', bottom=True, top=True, left=True, right=True)
#pp.auto_adjust_xaxis_date(ax, ds['Time'])
#ax.set_ylim(-5, 5)
ax.set_xlabel('Time [year]')
ax.set_ylabel('LOS displacement [mm]')
#ax.grid(True)
fig.tight_layout()
# output
out_file = os.path.join('/data/GREENLAND/2022/GNET_TIMESERIES/kely_gnss_timeseries.pdf')
plt.savefig(out_file, bbox_inches='tight', transparent=True, dpi=900)
print(f'save to file: {out_file}')
# %%
