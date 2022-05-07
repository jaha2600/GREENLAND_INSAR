# Jasmine Hansen 2022 #
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
    parser = argparse.ArgumentParser(description='Extract date_steps')
    #make sure you hardcode the path or use $PWD/ in the commandline infront of file
    parser.add_argument('directory', type = str, help = 'dir with location of h5 file')
    parser.add_argument('filename', type = str, help = 'name of the file')
    return parser

parser = getparser()
args = parser.parse_args()
#%%
#change dir
dirs = args.directory
#dirs='/data/GREENLAND/2022/KANGER_TEST/mintpy/geo/'
#dirs = '/home/jasmine/JasmineShare/kanger/mintpy_summit/geo/'
os.chdir(dirs)

h5_file = args.filename
# import hdf5 file
#h5_dir = '/home/jasmine/JasmineShare/kanger/mintpy/timeseries.h5'

h5_dir = os.path.join(dirs,h5_file)
# put dates into a list 
with h5.File(h5_dir,'r') as f:
    #data = f['timeseries'][:]
    date_list = f['date'][:]
date_list = date_list.astype(int)

#dates = []
df = pd.DataFrame()

df['date_1'] = date_list[:,0]
df['date_2'] = date_list[:,1]
df['dates'] = df[['date_1', 'date_2']].apply(lambda row: '_'.join(row.values.astype(str)), axis=1)
df.drop(columns=['date_1', 'date_2'])
df.to_csv((os.path.join(dirs,'dates.csv')), index=True, header=False)

# %%
