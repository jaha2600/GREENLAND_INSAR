#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from mintpy.objects import ifgramStack
from mintpy.utils import plot as pp, utils as ut
from mintpy import view, plot_network
import h5py
# %%
view.main()
# %%
mp_dir = ('/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/INSAR/mintpy')
os.chdir(mp_dir)

ifgs = os.path.join(mp_dir, 'ifgramStack.h5')

#%%
h5 = h5py.File(ifgs,'r')
print(h5.attrs)
# %%
# plot all data related with one interferometric pair
view.main('./ifgramStack.h5 20200812_20200824 --ncols 3'.split())
# %%

# %%
