#%%
import os
import matplotlib.pyplot as plt
from mintpy.tsview import timeseriesViewer

# visualization functions
def tsview(fname, yx=None, figsize_img=[5, 4], figsize_pts=[5, 2]):
    """Plot input file using tsview.py"""
    cmd = 'tsview.py {} --ms 4 --noverbose --save'.format(fname)
    if yx is not None:
        cmd += ' --yx {} {}'.format(yx[0], yx[1])
    obj = timeseriesViewer(cmd)
    obj.configure()
    obj.figsize_img = figsize_img
    obj.figsize_pts = figsize_pts
    obj.plot()
    return obj

# %%


ts_file = os.path.expanduser('/home/jasmine/JasmineShare/kanger/mintpy_summit/timeseries.h5')
tsview(ts_file, yx=(840, 796), figsize_img=[4, 5])


# %%
