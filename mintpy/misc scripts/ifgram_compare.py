# script to try and difference different hdf5 data.
# import modules
#%%
import numpy as np
import h5py as h5 
import matplotlib.pyplot as plt
import pandas as pd
#from osgeo import gdal

#%%
##### ifgram.h5 file in inputs dir ####
h5 = h5.File('/home/jasmine/JasmineShare/kanger/mintpy_2/maskConnComp.h5','r')
mask = h5['mask']
plt.imshow(h5)

#%%
if_h5 = h5.File('/data/GREENLAND/2022/KANGER_TEST/mintpy/inputs/ifgramStack.h5', 'r')
#ts_h5_ion = h5.File('path', 'r')
# obtain keys which tell you the datasets in the file 
keys = list(if_h5.keys())
u_phase = if_h5['unwrapPhase']
coh = if_h5['coherence']
#date = if_h5['date']

# import second file with ion corr.
if_h5_ion = h5.File('/data/GREENLAND/2022/KANGER_TEST_ION/mintpy/inputs/ifgramStack.h5','r')
keys_i = list(if_h5_ion.keys())
u_phase_i = if_h5_ion['unwrapPhase']
coh_i = if_h5_ion['coherence']
#date_i = if_h5_ion['date']
#%%
# get datelists and can visually compare to check the interferogram lists are the same
date_list = if_h5['date'][:]
date_list_i = if_h5_ion['date'][:]

df = pd.DataFrame()
df['date_1'] = date_list[:,0]
df['date_2'] = date_list[:,1]
df['dates'] = df[['date_1', 'date_2']].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
df['date_1_i'] = date_list_i[:,0]
df['date_2_i'] = date_list_i[:,1]
df['dates_i'] = df[['date_1_i', 'date_2_i']].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
df.drop(columns=['date_1', 'date_2', 'date_1_i', 'date_2_i'])
#%% test difference
if df['dates'].equals(df['dates_i']) == True:
    print('yes')
    diff_df = pd.DataFrame()
    uph_list = []
    coh_list = []
    for i in range(len(df)):
        print('Working on {}/{}'.format(i+1, len(df)))
        uph = u_phase[i] - u_phase_i[i]
        uph = np.sum(uph)
        uph_list.append(uph)

        cohr = coh[i] - coh_i[i]
        cohr = np.sum(cohr)
        coh_list.append(cohr)

    diff_df['dates'] = df['dates']
    diff_df['unw_phase'] = uph_list
    diff_df['coher'] = coh_list

else:
    print('interferogram dates are different between runs, check date dataframe')

#test = u_phase[1] - u_phase_i[1]

#plt.imshow(test)
#%%
#### timeseries.h5 stores each timestep of your mintpy run, dates and timeseries datasets in file ####
# read in the timeseries hdf 5 file 
# ts_h5 = h5.File('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy/timeseries.h5', 'r')
#ts_h5_ion = h5.File('path', 'r')
# obtain keys which tell you the datasets in the file 
# keys = list(ts_h5.keys())
# timeseries = ts_h5['timeseries']
# dates = ts_h5['date']
#%%
# keys_ion = list(ts_h5_ion.keys())
# timeseries_ion = ts_h5_ion['timeseries']
# dates_ion = ts_h5_ion['date']
# can do timeseres.shape, timeseries.dtype etc.
# timeseries has different layers for different timeslices
# i.e. timeseries [0] will be your first timeseries step, and then dates[0] the corresponding date
# if arrays are the same size and dates are the same so you can just subtract one from another

# create table and then just compare the dates of the two files to see if same. 
""" dates_df = pd.DataFrame()
dates_df['dates'] = dates
dates_df['dates_ion'] = dates_ion
# %%
# if they are the same then you can just subtract corresponding timeseries steps from one another.
test = timeseries[0] - timeseries_ion[0]
plt.imshow(test) """

# this could be iterated into a loop where you difference each slice and then save them out as diff figures
# would be helpful if you could save out them as a geotiff which im not sure how to do yet
