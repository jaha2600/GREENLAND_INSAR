#!/usr/local/anaconda3/bin/python

#Script to run an image filter over a DEM and keep the georeferencing
#Type of filter can be changed from medfilt - see the scipy.signal information as to other filters and their configuration


#Edited by Jasmine Hansen 2018 from rasterio cookbook code from mapbox/rasterio-cookbook github
#Runs in python3.6

import sys
import rasterio
from scipy.signal import medfilt
import os
import argparse

#code to make it command line executable 
def getparser():
    parser = argparse.ArgumentParser(description="Run median filter on input GeoTiff")
    parser.add_argument('file', type=str, help='File')
    parser.add_argument('window_size', type=int, help='Filter Window Size - Must Be Odd No.')
    return parser

parser = getparser()
args = parser.parse_args()

filename = args.file
win_size = args.window_size


### OLD CODE IGNORE ##
# The location of the files that you want to run the filter over
#filenames = sys.argv[1]
#directory = "/data/ANTARCTICA_2020/coregistered_dems/berp/30m_coregistered/cloud_masked/"


# A list of all pathnames of files ending in "_clip" within directory 
# [-5:] refers to looking five letters in from the end of the filename (without the extension) - change this to be a unique idenitifer

#path_list = [os.path.join(directory, fname) for fname in os.listdir(directory) if os.path.splitext(fname)[0][-5:] == "_tomo"]
#path_list = [os.path.join(directory, fname) for fname in os.listdir(directory) if fname.endswith("DHDT_MOSAIC_30m.tif")]
# For each "_clip" file identified, tack a "_med9" extension onto the filename to create the output file.
### ##

# function that will run a median filter over the input geotiff 
def main():
    path_list = [filename]
    output_path_list = []
    for pathname in path_list:
        fname, ext = os.path.splitext(pathname)
        med_name = '_med{}'.format(win_size)
        output_path_list.append(fname + med_name + ext)
    
    
    # This loop runs the filter over the dems
    for inputname,outputname in zip(path_list, output_path_list):
        print(inputname, outputname)
    
        with rasterio.open(inputname) as src:
            array = src.read()
            profile = src.profile
    
        # apply a X by X median filter to each band
        filtered = medfilt(array, (1,win_size,win_size)).astype('float32')
    
        # Write to tif, using the same profile as the source
        with rasterio.open(outputname, 'w', **profile) as dst:
            dst.write(filtered)

if __name__ == "__main__":
    main()

