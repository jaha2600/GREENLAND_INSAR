# convert vertical and horizontal components to LOS.
import os
import subprocess
import numpy as np
from osgeo import gdal

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
def readFile(filename):
    dataset = gdal.Open(filename)
    cols = dataset.RasterXSize 
    rows = dataset.RasterYSize
    projection = dataset.GetProjection()
    geotransform = dataset.GetGeoTransform()
    xMin = geotransform[0]
    yMax = geotransform[3]
    xres = geotransform[1]
    yres = geotransform[5]
    data_raster = dataset.GetRasterBand(1)
    dataset_array = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(float)

    return xMin, yMax, dataset_array, xres, yres, projection
#%% mintpy directory
dirs = '/home/jasmine/JasmineShare/kanger/mintpy_summit/'


def get_ref_comps(mintpy_loc):
#%% create components from geo_geometry datda
# change dir 
    os.chdir(os.path.join(mintpy_loc,'geo'))
    lat_cmd = 'save_gdal.py {}geo/geo_geometryRadar.h5 -d latitude --of GTiff -o {}geo/latitude.tif'.format(dirs,dirs,dirs)
    subprocess.run(lat_cmd,shell=True)

    lon_cmd = 'save_gdal.py {}geo/geo_geometryRadar.h5 -d latitude --of GTiff -o {}geo/latitude.tif'.format(dirs,dirs,dirs)
    subprocess.run(lon_cmd,shell=True)
    #%%
    hei_cmd = 'save_gdal.py {}geo/geo_geometryRadar.h5 -d height --of GTiff -o {}geo/height.tif'.format(dirs,dirs,dirs)
    subprocess.run(hei_cmd,shell=True)


# then if its a raster dataset put it into qgis to do calculation to los:
# los = (data_e * longitude.tif)+(data_n * latitude.tif)+(data_u * height.tif)

# if its a timeseries dataset then use this command in commandline to get vals of geotiffs at locations 
# gdallocationinfo uvg_rock_kanger_4326.tif -geoloc -50.838 67.078
# then do calculation with these lon lat height values and the dataset 
lon_loc = 
lat_loc = 
hei_loc = 

gnss_e =
gnss_n =
gnss_u = 

gnss_los = (gnss_e * lon_loc)+(gnss_n * lat_loc)+(gnss_u * hei_loc)

# for gnss timeseries data 
