#!/bin/bash

# load modules
ml purge
ml gcc/10.2.0
ml anaconda

# create enivoronment for mintpy
conda create -n mintpy -y
conda activate mintpy


# install mintpy 
conda install -c conda-forge mintpy -y
# install pyaps3 for ERA5 correciton (may already be installed in mintpy - check)
conda install -c conda-forge pyaps3 -y

#ERA5 correction
# user has to make account with CDS and accept data license 'https://cds.climate.copernicus.eu/user/register'
# check instructions below to add file in home directory and create .cdsapirc file
#https://github.com/insarlab/pyaps#2-account-setup-for-era5

# change the key to be your own key from the website
# check this works correctly (\n should execute a new line)
echo -e "url: https://cds.climate.copernicus.eu/api/v2\nkey: 128558:1342efd7-d87c-41f4-a2c2-10a847ff7080" >> ~/.cdsapirc