import os
import subprocess
import numpy as np
# import velocity and incidence angle files
# check if geotiffs exits
# if dont exist then generate them using save_gdal from mintpy 
# then import and use rasterio or gdal to do mathmatics 
dir = /path/to/mintpy_dir/
os.chdir(os.path.join(dir,'geo'))
vel_file = os.path.join(dir,'geo_velocity.tif')

if os.path.exists(vel_file) == True:
    print("{} already exists".format(vel_file))
else:
   cmd = 'geo_velocity.h5 -d --of GTiff -o geo_velocity.tif'
   subprocess.run(cmd,shell=True)
   print('geo_velocity.tif created')

# create incidence angle geotiff
inc_cmd = 'save_gdal.py geo_geometryRadar.h5 -d incidenceAngle --of GTiff -o incidenceAngle.tif'
subprocess.run(inc_cmd,shell=True)

# run math on incidence angle file
inc_2_cmd = 'gdal_calc.py -A incidenceAngle.tif --outfile=ic2.tif --calc="A*(3.141592653589793/180)"'
subprocess.run(inc_2_cmd)

#V_u = V_los / cos(inc_angle)
vel_cmd = 'gdal_cal.py -A geo_velocity.tif -B ic2.tif --calc="A/(numpy.cos/B)"' 
subprocess.run(vel_cmd)

# to get other components : 
#ve = np.sin(inc_angle) * np.sin(az_angle) * -1
#vn = np.sin(inc_angle) * np.cos(az_angle)
#vu = np.cos(inc_angle)