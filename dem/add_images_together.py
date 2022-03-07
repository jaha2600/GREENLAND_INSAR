#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 12:19:49 2021

@author: jasmine
"""

import rasterio
import sys, os
import argparse

def getparser():
    parser = argparse.ArgumentParser(description='combine raster files together')
    parser.add_argument('image_1', type = str, help = 'path to tif 1')
    parser.add_argument('image_2', type = str, help = 'path to tif 2')
    
    return parser

parser = getparser()
args = parser.parse_args()

tif_1 = args.image_1 
tif_2 = args.image_2

with rasterio.open(tif_1) as src:
    t1 = src.read(1)
    t1_meta = src.profile
with rasterio.open(tif_2) as src2:
    t2 = src2.read(1)
    t2_meta = src2.profile
    
    
comb_image = t1 + t2

root = os.path.split(tif_1)[0]
outfile_name = os.path.join(root, 'loc_image.tif')

with rasterio.open(outfile_name, 'w', **t1_meta) as dst:
         dst.write(comb_image,1)
