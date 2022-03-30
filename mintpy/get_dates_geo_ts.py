# short script to extract the timesteps of the timeseries h5 file to a textfile
#%%
import h5py as h5
import pandas as pd 
import os
import subprocess
#change dir
os.chdir('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/')
# import hdf5 file
h5_dir = '/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/geo_timeseries_ERA5_ramp_demErr.h5'
with h5.File(h5_dir,'r') as f:
    #data = f['timeseries'][:]
    date_list = f['date'][:]

dates = []
date_list = date_list.astype(int)
for i,f in enumerate(date_list):
    d = str(date_list[i]).strip("[]")
    dates.append(d)

date_df2 = pd.DataFrame()
date_df2['dates'] = date_list
#date_df2.to_csv('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/dates.csv', index=False, header=False)

#%%
# then run save_gdal.py for each date in the timeseries
for f in date_df2['dates']:
    cmd = 'save_gdal.py ./geo_timeseries_ERA5_demErr.h5 -d {} --of GTiff -o geo_ts_ERA5_demErr_{}' .format(f,f)
    print(cmd)
    subprocess.run(cmd,shell=True)

# %%
