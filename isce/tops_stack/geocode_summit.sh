#!/bin/bash

# Written by: Jasmine Hansen 2022 - jaha2600@colorado.edu
# Purpose: This script submits a job on RMACC Summit. Can be used with other HPC systems if SBATCH/scheduling commands are changed.   
#SBATCH --account=ucb62_summit3      # Summit allocation
#SBATCH --partition=shas    # Summit partition
#SBATCH --time=24:00:00           # Max wall time
#SBATCH --nodes=1          # Number of Nodes
#SBATCH --ntasks=4          # Number of tasks per job

#SBATCH --job-name=sstack      # Job submission name
#SBATCH --mail-type=END            # Email user when job finishes
#SBATCH --mail-user=jaha2600@colorado.edu        # Email address of user
# load modules and conda env
ml purge
ml gcc/10.2.0
ml gnu_parallel/20210322
ml anaconda
conda activate isce2
# geocode the los.rdr file. can change this to geocode any file.
# bounding box the same as the one used in stackSentinel
geocodeGdal.py -l lat.rdr -L lon.rdr -f los.rdr -b '67.122314 69.035088 -54.830711 -48.040665' -t
# convert to correct projection and retain isce format
gdal_translate geo_los.rdr geo_los_4326.rdr -a_srs EPSG:4326 -of ISCE

imageMath.py --eval='sin(rad(a_0))*cos(rad(a_1+90));sin(rad(a_0)) * sin(rad(a_1+90));cos(rad(a_0))' --a=geo_los_4326.rdr -t FLOAT -s BIL -o geo_enu.rdr
gdal_translate geo_enu.rdr geo_enu.tif

# extract the value at the coordniate that you want
gdallocationinfo -geoloc geo_enu.rdr -50.9418 67.3779 > enu.txt
# if want to do from list of coordniantes do 
#cat coords.txt | gdallocationinfo -geoloc geo_enu.rdr 