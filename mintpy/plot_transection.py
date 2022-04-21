#%%
import os
import matplotlib.pyplot as plt
from mintpy.plot_transection import transectionViewer

#%%
# function for visualization
def plot_coherence_matrix(fname='./velocity.h5', start_lalo=None, end_lalo=None, start_yx=None, end_yx=None):
    """Plot input file using plot_coherence_matrix.py"""
    cmd = 'plot_transection.py {} --noverbose --fontsize 10 --figsize 9.5 4 '.format(fname)
    cmd += ' --start-lalo {} {}'.format(start_lalo[0], start_lalo[1]) if start_lalo is not None else ''
    cmd += ' --end-lalo {} {}'.format(end_lalo[0], end_lalo[1]) if end_lalo is not None else ''
    cmd += ' --start-yx {} {}'.format(start_yx[0], start_yx[1]) if start_yx is not None else ''
    cmd += ' --end-yx {} {}'.format(end_yx[0], end_yx[1]) if end_yx is not None else ''
    print(cmd)
    obj = transectionViewer(cmd)
    obj.configure()
    obj.plot()
    return obj

# %%
vel_file = os.path.expanduser('/data/GREENLAND/2022/KANGER_TEST_ION/mintpy/geo/geo_velocity.h5')
obj = plot_coherence_matrix(vel_file, start_lalo=[-50.8535, 67.0464], end_lalo=[-50.7520, 67.1156])

# %%
