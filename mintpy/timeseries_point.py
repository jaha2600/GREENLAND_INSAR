## Read/plot displacement time-series of one pixel from timeseries HDF5 file
#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from mintpy.utils import utils as ut, plot as pp
#plt.rcParams.update({'font.size': 12})
#%%
# work directory
#proj_dir = '/data/GREENLAND/2022/KANGER_TEST_ION/mintpy_2/'
proj_dir = '/home/jasmine/JasmineShare/kanger/mintpy_summit/'
os.chdir(proj_dir)
## file in radar coordinates
#geom_file = os.path.join(proj_dir, './inputs/geometryRadar.h5')
#ts_file = os.path.join(proj_dir, 'timeseries_ERA5_ramp_demErr.h5')

# file in geo coordinates
geom_file = None
ts_file = os.path.join(proj_dir, 'geo/geo_timeseries_ERA5_demErr.h5')

# read dates and displacement
# kely lat lon 66.98741821,-50.94483762
print(f'read from file: {ts_file}')
dates, dis, dis_std = ut.read_timeseries_lalo(lat=66.98741821, lon=-50.94483762, ts_file=ts_file, lookup_file=geom_file)
#%%
# plot
# dis edited to be in mm instead of cm 
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[6, 3])
ax.scatter(dates, dis*1000, marker='^', s=6**2, facecolors='none', edgecolors='k', linewidth=1.)

# axis format edited for ylim values. 
ax.tick_params(which='both', direction='in', bottom=True, top=True, left=True, right=True)
pp.auto_adjust_xaxis_date(ax, dates)
ax.set_ylim(-5, 5)
ax.set_xlabel('Time [year]')
ax.set_ylabel('LOS displacement [mm]')
fig.tight_layout()

# output
out_file = os.path.join(proj_dir, 'kely_ts.png')
plt.savefig(out_file, bbox_inches='tight', transparent=True, dpi=300)
print(f'save to file: {out_file}')
plt.show()
# %%
