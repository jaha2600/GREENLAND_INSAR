# script to try and difference different hdf5 data.
# import modules
#%%
import numpy as np
import h5py as h5 
import matplotlib.pyplot as plt
import pandas as pd
from osgeo import gdal
#%%
#### timeseries.h5 stores each timestep of your mintpy run, dates and timeseries datasets in file ####
# read in the timeseries hdf 5 file 
ts_h5 = h5.File('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/timeseries.h5', 'r')
#ts_h5_ion = h5.File('path', 'r')
# obtain keys which tell you the datasets in the file 
keys = list(ts_h5.keys())
timeseries = ts_h5['timeseries']
dates = ts_h5['date']
#%%
keys_ion = list(ts_h5_ion.keys())
timeseries_ion = ts_h5_ion['timeseries']
dates_ion = ts_h5_ion['date']
# can do timeseres.shape, timeseries.dtype etc.
# timeseries has different layers for different timeslices
# i.e. timeseries [0] will be your first timeseries step, and then dates[0] the corresponding date
# if arrays are the same size and dates are the same so you can just subtract one from another

#%%
# create table and then just compare the dates of the two files to see if same. 
dates_df = pd.DataFrame()
dates_df['dates'] = dates
dates_df['dates_ion'] = dates_ion
# %%
# if they are the same then you can just subtract corresponding timeseries steps from one another.
test = timeseries[0] - timeseries_ion[0]
plt.imshow(test)

# this could be iterated into a loop where you difference each slice and then save them out as diff figures
# would be helpful if you could save out them as a geotiff which im not sure how to do yet


##### ifgram.h5 file in inputs dir ####

