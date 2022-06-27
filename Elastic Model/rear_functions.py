#%% import modules
import numpy as np
import rasterio as rio
import os, sys, subprocess
import matplotlib.pyplot as plt
import pandas as pd
from math import cos, sin, asin, sqrt, radians
#%%
# import dhdt grid into array
dirs = '/Users/jasminehansen/Documents/Colorado/PhD_Work/2022/Greenland/DATASETS/SMITH_ICESAT2/ICESat1_ICESat2_mass_change_updated_2_2021/FOR_REAR/1000/'
fn = 'gris_dhdt_1000_4326.tif'

#%%

def calc_distance(lat1, lon1, lat2, lon2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * asin(sqrt(a))
    km = 6371 * c
    return km
#%%
# change calculation 
#2.5x360/(2pix6371) = 0.0225
def dhdt_grid_setup(dirs, fn, grid_rad_km):
    file = os.path.join(dirs,fn)
    with rio.open(file) as src:
        grid = src.read(1)
        grid_meta = src.profile
        grid_arr = np.array(grid)
    # convert nan to 0 as disc with no change?
    grid[np.isnan(grid)] = 0

    # dh/dt to mwe yr^-1? It should be dh/dt x 917/1000

    # convert to mwe by m/v = d expression - density of water 
    #grid_size_degrees = grid_meta['transform'][0]
   # grid_mwe = grid_arr*(grid_size_degrees*grid_size_degrees) * 1000
    grid_mwe = grid_arr * (917/1000)
    #convert to discs by multiplying by 4/pi
    grid_disc = grid_mwe * (4/np.pi)
    outfile = os.path.join(dirs,'gris_mwe_disc.tif')
    with rio.open(outfile, "w", **grid_meta) as dest:
        dest.write(grid_disc,1)
    # convert to xyz file 
    xyz_outfile = os.path.splitext(outfile)[0] + '.xyz'
    command='gdal_translate -of XYZ {} {}'.format(file, xyz_outfile)
    subprocess.run(command,shell=True)

    #
    # caclulate angular disc radius with equation from Bevis et al. 2016
    earth_radius = 6371
    #2.5x360/(2pix6371) = 0.0225
    alfa = 360*grid_rad_km/((2*np.pi) * earth_radius)
    alfa = str(alfa)
    #alfa_fortran = alfa.replace("e", "d")
    # %% build input file for REAR
    # format ELEMENT, lon, lat, disc  radius, rate 
    #%% read in surface change xyz into pandas dataframe 
    colnames=['long', 'lat', "rate (m/yr)"] 
    dmdt_df = pd.read_csv(xyz_outfile, delimiter=" ",names=colnames, header=None, quotechar='\0')
    dmdt_df['long'] = dmdt_df['long'] + 360
    dmdt_df = dmdt_df.fillna(0)
    dmdt_df['disc radius (deg)'] = alfa
    dmdt_df.insert(0, 'Element n.', range(1, 1+len(dmdt_df)))
    dmdt_df = dmdt_df.reindex(columns=['Element n.', 'long', 'lat', 'disc radius (deg)', 'rate (m/yr)'])
    # save out as file, original has 6 spaces as the delimeter
    end_file = os.path.splitext(outfile)[0] + '.dat'
    dmdt_df.to_csv(end_file, sep=' ' ,index=False)

    return alfa, end_file
#%%
alfa, end_file = dhdt_grid_setup(dirs,fn,0.05)

# %% edit input files for input_data_gf.inc input_data_map.inc
directory = '/Users/jasminehansen/Documents/Colorado/PhD_Work/Code/REAR/REAR-v1.0'
header_lines = 2
#%% directoryabove, alfa from above function, end_file is ice load model
def edit_rear_inputs(directory, alfa, end_file, header_lines):
    # edit input files for fortran for your own data
    # get alfa from previous function and put in fortran format
    alfa = str(alfa)
    # edit the input_data_gf.inc file for updated alfa 
    end_file = os.path.split(end_file)[1]
    # location of example gf file and then new file to be put into main directory
    gf_name = os.path.join(directory, 'ORIGINAL/input_data_gf.inc')
    gf_new_name = os.path.join(directory, 'input_data_gf.inc')

    with open(gf_name, 'r') as f:
        lines = f.readlines()
        lines[39] = "         alfa={}           ! Half-amplitude of the load (deg)\t\t     \n".format(alfa)
    with open(gf_new_name, "w") as f1:
        f1.writelines("%s\n" % file for file in lines)
    #%%
    #edit input_data_map.inc variables
    map_name = os.path.join(directory, 'ORIGINAL/input_data_map.inc')
    map_new_name = os.path.join(directory, 'input_data_map.inc')
    #header_lines = '1'
    with open(map_name, 'r') as m:
        lines2 = m.readlines()
        # ice file path - change the filename in DATA
        lines2[33]= ' character*200, parameter :: file_ice="./DATA/{}"   ! File of the ice model'.format(end_file)
        # number of header lines
        lines2[34] = ' integer, parameter :: NH_ICE={}                             ! Header lines in file_ice'.format(header_lines)
    with open(map_new_name, 'w') as f2:
        f2.writelines("%s\n" % file2 for file2 in lines2)

edit_rear_inputs(directory, alfa, end_file, header_lines)
# %% get output from REAR and process to csv file
def uvg2csv(file):
    file_root = os.path.splitext(file)[0]
    file_csv = file_root + '.csv'

    #%% # change delimiters to csv
    sed_cmd_1= "sed 's/  */ /g' {} > {}".format(file, file_csv)
    subprocess.run(sed_cmd_1,shell=True)
    #%%
    #  change if using on linux as -i flag on that but -i '' -e on mac osx
    sed_cmd_2= "sed -i ''  -e 's/ /,/g' {}".format(file_csv)
    subprocess.run(sed_cmd_2,shell=True)

    #%%
    sed_cmd_3= "sed -i'' -e '2d' {}".format(file_csv)
    subprocess.run(sed_cmd_3,shell=True)
    #%%
    #%% add column 
    df = pd.read_csv(file_csv)
    #%%
    # delete bad columns
    df = df.drop(df.columns[[0, 7, 8,9,10,11,12,13,14]], axis=1)
    #%%
    col_names = ['Lon','Lat','UrDOT','UthetaDOT','UlambdaDOT','NDOT']
    df.columns = col_names
    df['Lon360'] = df['Lon'] - 360
    #%%
    df.to_csv(file_csv, index=False)