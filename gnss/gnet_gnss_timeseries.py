
#%%
import pandas as pd
import matplotlib.pyplot as plt
#%%
# import data
ds = pd.read_csv('/data/GREENLAND/2022/GNET_TIMESERIES/KELY_NEU.csv')
# %%
plt.scatter(ds['Time'], ds['Up'])
# %%
import numpy as np

#fit polynomial models up to degree 5
model1 = np.poly1d(np.polyfit(ds.Time, ds.Up, 1))
model2 = np.poly1d(np.polyfit(ds.Time, ds.Up, 2))
model3 = np.poly1d(np.polyfit(ds.Time, ds.Up, 3))
model4 = np.poly1d(np.polyfit(ds.Time, ds.Up, 4))
model5 = np.poly1d(np.polyfit(ds.Time, ds.Up, 5))
#%%
#create scatterplot
polyline = np.linspace(1, 15, 50)
plt.scatter(ds.Time, ds.Up)

#add fitted polynomial lines to scatterplot 
plt.plot(polyline, model1(polyline), color='green')
plt.plot(polyline, model2(polyline), color='red')
plt.plot(polyline, model3(polyline), color='purple')
plt.plot(polyline, model4(polyline), color='blue')
plt.plot(polyline, model5(polyline), color='orange')
plt.show()

# %%
