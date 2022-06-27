Code for creating inputs and processing outputs for Regional Elastic Rebound Calculator (REAR) - Melini 

1. Starting with a geotiff of surface height change (dhdt) over chosen area of interest in EPSG:4326
2. Then run the function dhdt_grid_setup which generates the required input grid for REAR which is called gris_mwe_disc.dat
3. Copy this file into the DATA directory in your REAR installation 
4. Edit the two input files that exist for REAR using the function edit_rear_inputs. Inputs are location of rear installation, alfa and end file from dhdt_grid_setup function and the number of header lines in your .dat file (should be 2)
5. Following this go to REAR installation and check input files. Edit the grid size in the map inputs file to get finer scale output grid being producted
6. Run make gf 
7. Run make map and get output 
8. Run plot*.gmt5 script to get map output - check .ps figure
9. Take output file (uvg.dat) and then run function uvg2csv to convert that to a csv file and calulate new Longitude.
10. I import into QGIS and then generate a raster in there, and mask using the land use masks from bedmachine.