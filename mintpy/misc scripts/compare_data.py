# things you want to compare
# overall velocity map
# individual timesteps
#%%
# import modules
import h5py as h5
import pandas as pd 
import os
import subprocess
import argparse
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
#%%
# parser for command line entry
def getparser():
    parser = argparse.ArgumentParser(description='Extract geocoded timeseries steps')
    #make sure you hardcode the path or use $PWD/ in the commandline infront of file
    parser.add_argument('directory', type = str, help = 'dir with location of  geo timeseries h5 file')
    #parser.add_argument('filename', type = str, help = 'name of the geo timeseries file')
    return parser

parser = getparser()
args = parser.parse_args()
#%%
directory = '/home/jasmine/JasmineShare/kanger/mintpy_gacos/'
timeseries = 'timeseries_GACOS_demErr.h5'
velocity = 'velocity.h5'

directory_2 = '/home/jasmine/JasmineShare/kanger/mintpy_summit/'
timeseries_2 = 'timeseries_ERA5_demErr.h5'
velocity_2 = 'velocity.h5'
#%%
# functions
def read_ts(DIR,FILENAME):
    h5_dir = os.path.join(DIR,FILENAME)
    with h5.File(h5_dir,'r') as f:
        date_list = f['date'][:]
        date_list = date_list.astype(int)
        ts_data = f['timeseries'][:]

        return date_list, ts_data

def read_vel(DIR,FILENAME):
    h5_dir = os.path.join(DIR,FILENAME)
    with h5.File(h5_dir,'r') as f:
        vels = f['velocity'][:]
        vel_std = f['velocityStd'][:]

        return vels, vel_std

#def hist_fig(ds, title):
    # define window size, output and axes
    fig, ax = plt.subplots(figsize=[8,6])
    # set plot title
    ax.set_title("{}".format(title))
    # set x-axis name
    ax.set_xlabel("Vel (mm/yr)")
    # set y-axis name
    ax.set_ylabel("Normalized")
    ax.set_ybound
    # create histogram within output
    #N, bins, patches = ax.hist(vel_1.ravel(), bins=500, ) #initial color of all bins
    sns.histplot(vel_1.ravel(), bins=50, kde=True, stat='probability')
    # Iterate through all histogram elementa
plt.show()
#%%
# read in velocity datasets
vel_1, vel_std_1 = read_vel(directory, velocity)
vel_2, vel_std_2 = read_vel(directory_2, velocity_2)

# read in timeseries datasets
date_1, ts_1 = read_ts(directory, timeseries)
date_2, ts_2 = read_ts(directory_2, timeseries_2)
# %%
# check datelists are the same so comparison is good for ts 
date_1_df = pd.Series(date_1) 
date_2_df = pd.Series(date_2)
# returns True if the same 
equal = date_1_df.equals(date_2_df)

#%% 
# IF dates lists are identical then you can compare timesteps in timeseries
if equal == True:
    ts_diff = []
    for f in range(len(ts_1)):
        #print(f)
        # compare timestep creating a difference array
        diff = ts_1[f] - ts_2[f]
        ts_diff.append(diff)
    # create stack of differences for each timestep 
    ts_diff = np.stack(ts_diff, axis=0)
else:
    print('Timesteps do not match between datasets')

# compare velocity datasets
vel_difference = vel_1 - vel_2
# %%
# generate data

# velocity data

# define window size, output and axes
fig, ax = plt.subplots(figsize=[8,6])
# set plot title
ax.set_title("Some title")
# set x-axis name
ax.set_xlabel("X-Label")
# set y-axis name
ax.set_ylabel("Y-Label")

#ax.hist(vel_1.ravel(), bins=100, density=True)
sns.set()
sns.histplot(vel_1.ravel(), bins=50, kde=False, stat='probability', alpha=.7)
sns.histplot(vel_2.ravel(), bins=50, kde=False, stat='probability', alpha=.5, color='g')

# a is your data array
#hist, bins = np.histogram(vel_1.ravel(), bins=100, density=True)
#bin_centers = (bins[1:]+bins[:-1])*0.5
#plt.plot(bin_centers, hist)


# create histogram within output
#ax.hist(vel_1.ravel(), bins=100) #initial color of all bins
#sns.histplot(vel_1.ravel(), bins=50, kde=True, stat='probability')
# Iterate through all histogram elementa
plt.show()
# histograms of original velocity datasets
# figures of difference map for velocity 
# statistics for velocity differences
# ts difference maps 
# statistics for each ts layer difference 

# %%
