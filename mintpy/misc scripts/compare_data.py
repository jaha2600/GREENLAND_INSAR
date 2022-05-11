# things you want to compare
# overall velocity map
# individual timesteps

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
    #parser.add_argument('filename', type = str, help = 'name of the geo timeseries file')
    return parser

parser = getparser()
args = parser.parse_args()

dir = 
filename =

# read in hdf5 files and then subtract from one another
def read_ts(DIR,FILENAME):
    h5_dir = os.path.join(DIR,FILENAME)
    with h5.File(h5_dir,'r') as f:
        date_list = f['date'][:]
        date_list = date_list.astype(int)
        ts_data = f['timeseries'][:]

        return date_list, ts_data

