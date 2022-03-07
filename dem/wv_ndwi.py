#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 23 13:39:44 2021

@author: jasmine
"""

#import required libraries
import rasterio
from rasterio import plot
import matplotlib.pyplot as plt
import numpy as np
from numpy import *
import os, sys
# import bands seperately 
# for ndwi the bands are (coastal - nir2)/(coastal + nir2) or use blue instead of coastal

with rasterio.open('/Bhaltos/GREENLAND_JASMINE/2021/mike_class/LC08_L1TP_007013_20160201_20200907_02_T1_B6.TIF') as src:
    swir = src.read(1)
#grd = rasterio.open(image)


with rasterio.open(image)
coastal = grd.read(1)
nir2 = grd.read(7)
green = grd.read(5)



ndwi = (green - swir) / (green + swir)

mask = np.copy(ndwi)
where_are_nans = isnan(mask)


mask[mask < 1] = 1
mask [mask != 1] = 0

mask[where_are_nans] = nan

outfile = ''
#export ndvi image
ndwiImage = rasterio.open('/data/ndviImage2.tif','w',driver='Gtiff',
                          width=grd.width, 
                          height = grd.height, 
                          count=1, crs=grd.crs, 
                          transform=grd.transform, 
                          dtype='float64')
ndwiImage.write(mask,1)
ndwiImage.close()

# make the mask 

os.sys()