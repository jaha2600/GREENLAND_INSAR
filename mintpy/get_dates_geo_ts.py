# Jasmine Hansen 2022 #
# identify timesteps in geocoded timeseries hdf5 file and create a geotiff for each timestep
#%%
# import modules
import h5py as h5
import pandas as pd 
import os
import subprocess
import argparse
#%%
# parser for command line entry
def getparser():
    parser = argparse.ArgumentParser(description='Extract geocoded timeseries steps')
    #make sure you hardcode the path or use $PWD/ in the commandline infront of file
    parser.add_argument('directory', type = str, help = 'dir with location of  geo timeseries h5 file')
    parser.add_argument('filename', type = str, help = 'name of the geo timeseries file')
    return parser

parser = getparser()
args = parser.parse_args()
#%%
#change dir
#dirs = args.directory
#dirs='/data/GREENLAND/2022/KANGER_TEST/mintpy/geo/'
dirs = '/home/jasmine/JasmineShare/kanger/mintpy/'
os.chdir(dirs)

h5_file = args.filename
# import hdf5 file
h5_dir = '/home/jasmine/JasmineShare/kanger/mintpy/timeseries.h5'
#h5_dir = os.path.join(dirs,'geo_timeseries_ERA5_ramp_demErr.h5')
# put dates into a list 
with h5.File(h5_dir,'r') as f:
    #data = f['timeseries'][:]
    date_list = f['date'][:]

#dates = []
date_list = date_list.astype(int)
#for i,f in enumerate(date_list):
 #   d = str(date_list[i]).strip("[]")
  #  dates.append(d)

# add list to pandas dataframe
date_df2 = pd.DataFrame()
date_df2['dates'] = date_list

# option below to save date list as csv file if you want
#date_df2.to_csv('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/dates.csv', index=False, header=False)

#%%
# then run save_gdal.py for each date in the timeseries to create output geotiff
for f in date_df2['dates']:
    cmd = 'save_gdal.py geo_timeseries_ERA5_ramp_demErr.h5 -d timeseries-{} --of GTiff -o geo_ts_ERA5_demErr_{}.tif'.format(f,f)
    #print(cmd)
    subprocess.run(cmd,shell=True)

