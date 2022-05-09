#%%
import os
import numpy as np
import matplotlib.pyplot as plt
from mintpy.utils import readfile, utils as ut
plt.rcParams.update({'font.size': 12})

work_dir = os.path.expanduser('/home/jasmine/JasmineShare/kanger/mintpy_summit/')
os.chdir(work_dir)
print('Go to directory:', work_dir)

#%%
# geocoded file paths [for input dataset in radar coordinates]
ts_file = 'geo/geo_timeseries_ERA5_demErr.h5';  date1, date2 = '20160101', '20171022'
vel_file = 'geo/geo_velocity.h5'
mask_file = 'geo/geo_maskTempCoh.h5'
geom_file = 'geo/geo_geometryRadar.h5'

# read displacement data between two dates in meters from time series file
#dis, atr = readfile.read(ts_file, datasetName=date2)
#dis -= readfile.read(ts_file, datasetName=date1)[0]
# OR read displacement data in meters per year from velocity file
dis, atr = readfile.read(vel_file)

# read geometry data: latitude, longitude, incidence angle and azimuth angle
lat, lon = ut.get_lat_lon(atr)
inc_angle = readfile.read(geom_file, datasetName='incidenceAngle')[0] * np.pi / 180.
az_angle  = readfile.read(geom_file, datasetName='azimuthAngle')[0] * np.pi / 180.

# mask out invalid / unreliable pixels
mask = readfile.read(mask_file)[0]
mask *= ~np.isnan(inc_angle)
dis[mask == 0] = np.nan
lat[mask == 0] = np.nan
lon[mask == 0] = np.nan
inc_angle[mask == 0] = np.nan
az_angle[mask == 0] = np.nan

# calculate the unit vector for InSAR displacement [positive for motion toward from satellite]
ve = np.sin(inc_angle) * np.sin(az_angle) * -1
vn = np.sin(inc_angle) * np.cos(az_angle)
vu = np.cos(inc_angle)
# %%
## PLOT ##
fig, axs = plt.subplots(nrows=1, ncols=6, figsize=[18, 4], sharey=True)
titles = ['Latitude', 'Longitude', 'Displacement', 'V_east', 'V_north', 'V_up']
for ax, data, title in zip(axs, [lat, lon, dis, ve, vn, vu], titles):
    im = ax.imshow(data, interpolation='nearest')
    fig.colorbar(im, ax=ax, location='bottom')
    ax.set_title(title)
fig.tight_layout()
plt.show()

# %%fffdfgdfg


out_file = os.path.abspath(f'dis_vel.txt')
header =  'number of points: {}\n'.format(np.sum(mask))
header += 'reference pixel in in (lat, lon): ({}, {})\n'.format(atr['REF_LAT'], atr['REF_LON'])
header += 'latitude,longitude,displacement[m],Vz,Vn,Ve'
data = np.hstack((
    lat[mask].reshape(-1, 1),
    lon[mask].reshape(-1, 1),
    dis[mask].reshape(-1, 1),
    ve[mask].reshape(-1, 1),
    vn[mask].reshape(-1, 1),
    vu[mask].reshape(-1, 1),
))
print('writing to text file: {}'.format(out_file))
#np.savetxt(out_file, data, fmt='%10.6f', delimiter=',', header=header)
np.savetxt(out_file, data, delimiter=',', header=header)

print('finished writing.')



# The saved text file is shown as below:
with open(out_file, 'r') as f:
    head = ''.join([next(f) for x in range(15)])
print(head)

#%%
## generate output geotiff file using rasterio
lat_1 = lat[mask].reshape(-1, 1)
lon_1 = lon[mask].reshape(-1, 1)

lat_r = lat_1.reshape(6147,7061)
#%%
pixel_size = 
transform = from_origin(472137, 5015782, 0.5, 0.5)

new_dataset = rasterio.open('test1.tif', 'w', driver='GTiff',
                            height = arr.shape[0], width = arr.shape[1],
                            count=1, dtype=str(arr.dtype),
                            crs='+proj=utm +zone=10 +ellps=GRS80 +datum=NAD83 +units=m +no_defs',
                            transform=transform)

new_dataset.write(arr, 1)
new_dataset.close()