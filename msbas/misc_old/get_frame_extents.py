#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 12:46:04 2021

@author: jasmine
"""

from osgeo import ogr 
import os, sys, glob
import numpy as np

dirs = '/data/GREENLAND/INSAR/'
files = glob.glob(os.path.join(dirs,'asf_int*.shp'))

extent_list = []
file_list = []
outfile_list = []
for f in files:
    inDriver = ogr.GetDriverByName("ESRI Shapefile")
    inDataSource = inDriver.Open(f, 0)
    inLayer = inDataSource.GetLayer()
    extents = inLayer.GetExtent()
    extent = str(extents[0]) + ', ' + str(extents[3]) + ', ' + str(extents[1]) + ', ' + str(extents[2]) 
    filename = os.path.splitext(os.path.basename(f))[0]
    extent_list.append(extent)
    file_list.append(filename)
    
    overall_str = str(filename) + ' ' + str(extent)
    outfile_list.append(overall_str)
    
    
savepath = os.path.join(dirs,'path_frame_extents.txt') #Same as the asc.txt

np.savetxt(savepath, outfile_list, fmt="%s", delimiter=' ', newline='\n')

