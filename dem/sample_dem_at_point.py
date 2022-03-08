#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 12:03:27 2022

@author: jasminehansen
"""

## https://www.earthdatascience.org/courses/use-data-open-source-python/spatial-data-applications/lidar-remote-sensing-uncertainty/extract-data-from-raster/

import os, argparse
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import numpy.ma as ma
import pandas as pd
import rioxarray as rxr
import geopandas as gpd
# Rasterstats contains the zonalstatistics function
# that you will use to extract raster values
import rasterstats as rs
from matplotlib.patches import Patch  # for custom legend
import seaborn as sns
import math
from math import ceil  # determine correct number of subplot



def getparser():
    parser = argparse.ArgumentParser(description="Extract Points from DEMs")
    parser.add_argument('dem_dir', type=str, help='DEM Directory')
    parser.add_argument('shapefile',type=str, help ='Path and name of point shapefile')
    return parser

parser = getparser()
args = parser.parse_args()

DEM_DIRECTORY = args.dem_dir
SHP_PATH = args.shapefile

DEM_DIRECTORY = '/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/SMB_PROJECT/Antarctica/dem/'
# Set consistent plotting style
sns.set_style("white")
sns.set(font_scale=1.5)

# import shapefile points
SHP_PATH = '/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/SMB_PROJECT/Antarctica/dem/berp_sample_points_3031.shp'
shp = gpd.read_file(SHP_PATH)
# check its a points layer
shp.geom_type.head()

# create master df to append to at the end of each loop
master_df = pd.DataFrame()

directory = DEM_DIRECTORY
path_list = [os.path.join(directory, fname) for fname in os.listdir(directory) if fname.endswith(".tif")]

for i, file in enumerate(path_list):
    number = i+1
    number_dems = len(path_list)
    dem_id = os.path.splitext(os.path.basename(file))[0]
    print('File {}/{}'.format(number,number_dems))
    print('Working On {}'.format(dem_id))
    
    dem = rxr.open_rasterio(file,masked=True).squeeze()
    
    # extract statistics for each location.
    # add .values after an xarray object turns it into a numpy array
    # read into reasoning behind stats as it should just be one value? Perhaps is as getting over buffered area and not point loc.
    heights = rs.zonal_stats(SHP_PATH, dem.values, nodata=-9999, affine = dem.rio.transform(), geojson_out=True,copy_properties=True,stats="count min mean max median")
    
                                       
    # convert list to pandas geodataframe 
    heights_gdf = gpd.GeoDataFrame.from_features(heights)
    heights_gdf['lon'] = heights_gdf.geometry.apply(lambda p: p.x)
    heights_gdf['lat'] = heights_gdf.geometry.apply(lambda p: p.y)


    # convert to df
    heights_df = pd.DataFrame(heights_gdf)
    heights_df = heights_df.drop(columns=['count','min','max','median'])
    col_name = '{}'.format(dem_id)
    id_col = {'image_id': col_name}
    heights_df = heights_df.assign(**id_col)
    date = dem_id.split('_')[0]
    date_col = {'date': date}
    heights_df = heights_df.assign(**date_col)
    
    # append to the end of the master dataframe
    master_df = pd.concat([master_df, heights_df])
    # remove lines with no elev vals in 
    master_df = master_df.dropna(subset=['mean'])
    #master_df['date'] = pd.to_datetime(master_df['date'],format='%Y%m%d')
    master_df['date'] = pd.to_datetime(master_df['date'],format='%Y%m%d')

    
    
   # id_list = np.unique(master_df['id']).tolist()
   # test = master_df.query('id=="1"')
    
# slice master dataframe by point id to create dict of df that you can access
df_dict = {}

for ids in master_df['id'].unique():
    # create a dict with all of the sliced dataframes
    df_dict[ids] = master_df[  master_df['id'] == ids ]
    # access one indiviual df by doing df_sliced_dict['id'] i.e. 1,2,3,3,5
    
# save out total data
#outname = os.path.join(DEM_DIRECTORY, 'sampled_points.csv')
# then save the dataframe as a csv file
#master_df.to_csv(outname, sep=',', index=False,header=True)


# iterate through dictionary and plot
col_nums = 2  # how many plots per row
row_nums = math.ceil(len(df_dict) / col_nums)  # how many rows of plots

dict_keys = [k for k in df_dict.keys()]

plt.figure(figsize=(11,8.5))

for i, (k, v) in enumerate(df_dict.items(), 1):
    plt.subplot(row_nums, col_nums, i)  # create subplots
    p = sns.scatterplot(data=v, x='date', y='mean')
   # p = sns.scatterplot(data=v, x='date', y='mean', hue='cat', palette=cmap)
   # p.legend_.remove()  # remove the individual plot legends
    plt.title(f'Point ID: {k}')
    plt.tight_layout()
    plt.xticks(rotation=50)
    ax = plt.gca()
    plt.plot(v['date'], v['mean'])
        
fig = p.get_figure()

testdir = os.path.join(DEM_DIRECTORY,'timeseries_plots.png')

#fig.savefig(testdir,dpi=200)     
    
    
    
    
    

