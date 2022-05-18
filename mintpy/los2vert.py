
#%%
import os
import subprocess
import numpy as np
from osgeo import gdal
# import velocity and incidence angle files
# check if geotiffs exits
# if dont exist then generate them using save_gdal from mintpy 
# then import and use rasterio or gdal to do mathmatics 

#%% mintpy directory
dirs = '/home/jasmine/JasmineShare/kanger/mintpy_summit/'

# change dir and check for vel geotiff.
os.chdir(os.path.join(dirs,'geo'))
vel_file = os.path.join(dirs,'geo_velocity.tif')

# if os.path.exists(vel_file) == True:
#     print("{} already exists".format(vel_file))
# else:
#    cmd = 'save_gdal.py {}geo_velocity.h5 --of GTiff -o {}geo_velocity.tif'.format(dir,dir)
#    subprocess.run(cmd,shell=True)
#    print('geo_velocity.tif created')

#%% functions
def writeFile(filename,rasterOrigin,pixelWidth,pixelHeight,geoprojection,data):
        cols = data.shape[1]
        rows = data.shape[0]
        originX = rasterOrigin[0]
        originY = rasterOrigin[1]
        
        #(x,y) = data.shape
        format = "GTiff"
        driver = gdal.GetDriverByName(format)
        # you can change the dataformat but be sure to be able to store negative values including -9999
        dst_datatype = gdal.GDT_Float32
        dst_ds = driver.Create(filename,cols,rows,1,dst_datatype)
        dst_ds.GetRasterBand(1).WriteArray(data)
        dst_ds.SetGeoTransform((originX, pixelWidth, 0, originY, 0, pixelHeight))
        dst_ds.SetProjection(geoprojection)
        dst_ds.GetRasterBand(1).SetNoDataValue(nodata_value)


#%% create incidence angle geotiff
inc_cmd = 'save_gdal.py {}geo/geo_geometryRadar.h5 -d incidenceAngle --of GTiff -o {}geo/incidenceAngle.tif'.format(dirs,dirs,dirs)
print(inc_cmd)
subprocess.run(inc_cmd,shell=True)
#%%
# run math on incidence angle file
#inc_2_cmd = 'gdal_calc.py -A incidenceAngle.tif --outfile=ic2.tif --calc="A*(3.141592653589793/180)"'
#subprocess.run(inc_2_cmd,shell=True)

#%% open incidence angle geotiff and do math on it. 
dataset = gdal.Open('incidenceAngle.tif')
    #information about the raster
cols = dataset.RasterXSize 
rows = dataset.RasterYSize
band_no = dataset.RasterCount
driver = dataset.GetDriver().LongName
projection = dataset.GetProjection()
geotransform = dataset.GetGeoTransform()
xres = geotransform[1]
yres = geotransform[5]
xMin = geotransform[0]
yMax = geotransform[3]
xMax = xMin + (dataset.RasterXSize/geotransform[1])
yMin = yMax + (dataset.RasterXSize/geotransform[5])
dataset_extent = (xMin, xMax, yMin, yMax)
data_raster = dataset.GetRasterBand(1)
#nodata_value = data_raster.GetNoDataValue()
nodata_value = np.nan
dataset_array = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(float)
#%% do math on the incidence angle file
ic2 = dataset_array * (np.pi/180)
ic3 = np.cos(ic2)
#%%
# mask ic3
mask_cmd = 'save_gdal.py {}geo/geo_maskTempCoh.h5 --of GTiff -o {}geo/geo_maskTempCoh.tif'.format(dirs,dirs,dirs)
print(mask_cmd)
subprocess.run(mask_cmd,shell=True)


#%% run final calulation with velocity and ic3.tif 
#V_u = V_los / cos(inc_angle)
vel_cmd = 'gdal_calc.py -A geo_velocity.tif -B ic3.tif --outfile=v.tif --calc="A/B"' 
subprocess.run(vel_cmd,shell=True)

vel_mask_cmd = 'gdal_calc.py -A v.tif -B geo_maskTempCoh.tif --outfile=Vu.tif --calc="A*B"' 
subprocess.run(vel_mask_cmd,shell=True)

# to get other components : 
#ve = np.sin(inc_angle) * np.sin(az_angle) * -1
#vn = np.sin(inc_angle) * np.cos(az_angle)
#vu = np.cos(inc_angle)
# %%
