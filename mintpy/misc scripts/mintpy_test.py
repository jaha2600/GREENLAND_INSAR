#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from mintpy.objects import ifgramStack
from mintpy.utils import plot as pp, utils as ut
from mintpy import view, plot_network
import h5py
# %%
#view.main()
# %%
dirs = '/data/GREENLAND/2022/KANGER_TEST/mintpy/inputs/'
os.chdir(dirs)
h5_dir = os.path.join(mint_dir, 'inputs/ifgramStack.h5')

# %%
with h5py.File(h5_dir,'r') as f:
    #data = f['timeseries'][:]
    date_list = f['date'][:]

dates = []
date_list = date_list.astype(int)
for i,f in enumerate(date_list):
    d = str(date_list[i]).strip("[]")
    dates.append(d)

# %%
# loop to create figures of each interferogram, save out and rename
for d in dates:
    cmd = ('./ifgramStack.h5 {} --save --ncols 3').format(d)
    view.main(cmd.split())
    # plot all data related with one interferometric pair
    #view.main('./ifgramStack.h5 20200812_20200824 --save --ncols 3'.split())
    # old filename 
    fn_o = os.path.join(dirs, 'unwrapPhase.png')
    fn_n = os.path.join(dirs, 'unwrapPhase_{}_fig.png'.format(d))
    os.rename(fn_o, fn_n)

# %%
