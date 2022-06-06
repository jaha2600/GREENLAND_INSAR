#%%
from functions import *
import os
import rasterio as rio
import numpy as np

# clip to same area and resample to same size
# then import, flatten, and put as columns in pandas df
# then run rank and compare how correlated they are
#%%
dirs = '/home/jasmine/JasmineShare/kanger/mintpy_summit/geo/'
dir2 = '/home/jasmine/JasmineShare/kanger/dem/'
fn = 'geo_velocity_m.tif'
fn2 = 'glo_30.dem.wgs84'
total = os.path.join(dirs,fn)
total2 = os.path.join(dir2,fn2)

df2 = pd.DataFrame()
with rio.open(total) as src:
    grid = src.read(1)
    grid_meta = src.profile
    grid_arr = np.array(grid)
grid_arr = grid_arr.flatten()
#%%
df = pd.DataFrame()
df['a'] = grid_arr.tolist()
#%%
with rio.open(total2) as src2:
    grid = src2.read(1)
    grid_meta = src2.profile
    grid_arr_2 = np.array(grid)

grid_arr_2 = grid_arr_2.flatten()


#%%
if j == 0:
    df[j] = grid_arr.tolist()
else: 
    df2[j] = grid_arr.tolist()
    df.join(df2.set_index(df.index[-len(df2):])


list = [total,total2]
# %%
df = arr_to_df(list)
#%%
display_correlation(df)
display_corr_pairs(df)
# %%
