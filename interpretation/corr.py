#%%
from functions import *
import os

#%%
dirs = '/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/DATASETS/SMITH_ICESAT2/ICESat1_ICESat2_mass_change_updated_2_2021/dhdt/'
fn = 'gris_dhdt_4326.tif'
total = os.path.join(dirs,fn)
list = [total,total]
# %%
df = arr_to_df(list)

display_correlation(df)
display_corr_pairs(df)
# %%
