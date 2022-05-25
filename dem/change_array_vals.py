

#import modules needed
from osgeo import gdal
import numpy as np
import os
#from numpy import *
#from pygeotools.lib import iolib, warplib
#function to convert numpy array to geotiff.


directory = '/data/GREENLAND/mike_class/coreg/v2/'
path_list = [os.path.join(directory, fname) for fname in os.listdir(directory) if fname.endswith("2017_dif_2m_med9_bedrk_corr.tif")]
grid = '/data/GREENLAND/2022/DEMS/for_summit/correct_nodata/cop_dem/dem.tif'

for i, grid in enumerate(path_list):
    print(grid)
    #open raw dem in gdal to get specifications.
    dataset = gdal.Open(grid)
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
    print('extent: ',dataset_extent)
    #get data
    data_raster = dataset.GetRasterBand(1)
    #get no data value
    nodata_value = data_raster.GetNoDataValue()
    #Convert raster to array
    dataset_array = dataset.GetRasterBand(1).ReadAsArray(0,0,cols,rows).astype(np.float)
    array = np.copy(dataset_array)
    new_nodata_value = -32768
    array[array == nodata_value] = new_nodata_value
    # check for NaN flag... 
    is_nans = np.isnan(np.min(array))
    
#    if is_nans == False :
#        print('Numerical nodata value')
#        #check its lower and not a nodata value of 0
#        nodata_values = nodata_value
#        binary_mask[binary_mask > nodata_values] = 1
#        binary_mask[binary_mask != 1] = 0
#       # min_value = np.min(binary_mask)
#        #binary_mask[binary_mask == min_value] = np.nan
#    else:
#        print('NaN is nodata value')
#        #binary_mask[binary_mask != np.nan] = -9999
#        #binary_mask[binary_mask != 1] = 0
#        
#        binary_mask[binary_mask > 0] = 1
#        binary_mask[binary_mask < 0] = 1
#        binary_mask[binary_mask != 1] = 0


    # generate the new filename
    output_section = os.path.split(grid)[1]
    
    #save out this files
    #binary_output_filename = os.path.join(os.path.splitext(output_section)[0] + '_hole_template.tif')
    output_filename = os.path.join(os.path.splitext(output_section)[0] + ('_new.tif'))
    output_new_name_final = os.path.join((os.path.split(grid)[0]), output_filename)
    
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
    
    
 

    writeFile(output_new_name_final,(xMin,yMax),xres,yres,projection,np.array(array,dtype=float))

    
    
    
