#%%
from functions import *
import os

#%%
dirs = '/home/jasmine/JasmineShare/kanger/mintpy_summit/geo/'
dir2 = '/home/jasmine/JasmineShare/kanger/dem/'
fn = 'geo_velocity_m.tif'
fn2 = 'glo_30.dem.wgs84'
total = os.path.join(dirs,fn)
total2 = os.path.join(dir2,fn2)

list = [total,total2]
# %%
df = arr_to_df(list)
#%%
display_correlation(df)
display_corr_pairs(df)
# %%
