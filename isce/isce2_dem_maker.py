
#%%
# install dev version from 
#https://github.com/ACCESS-Cloud-Based-InSAR/dem-stitcher
# after this then install isce2 and lxml using: mamba install -c conda-forge isce2 lxml (can switch mamba for conda)
# then this script follows this tutorial for isce-2 
#https://github.com/ACCESS-Cloud-Based-InSAR/dem-stitcher/blob/dev/notebooks/Staging_a_DEM_for_ISCE2.ipynb

# import modules
from dem_stitcher.stitcher import stitch_dem
import rasterio
import matplotlib.pyplot as plt
from pathlib import Path
import subprocess
import site
from lxml import etree
import isce
from shapely.geometry import box
import numpy as np

#jh added parser march 10th 2022
import os, subprocess
import argparse
def getparser():
    parser = argparse.ArgumentParser(description='Create DEM for ISCE2')
    #make sure you hardcode the path or use $PWD/ in the commandline infront of file
    parser.add_argument('DEM_NAME', type = str, help = 'pick from srtm_v3, nasadem, glo_30, 3dep, ned1')
    parser.add_argument('LONMIN', type=str, help = 'format is lonmin latmin lonmax latmin')
    parser.add_argument('LATMIN', type=str)
    parser.add_argument('LONMAX', type=str)
    parser.add_argument('LATMIN', type=str) 
    parser.add_argument('--gtif', action='store_true',help='Optional Flag will save geotiff version for viewing')
    return parser

parser = getparser()
args = parser.parse_args()

dem_name = args.DEM_NAME 
lonmin = args.LONMIN 
latmin = args.LATMIN 
lonmax = args.LONMAX 
latmin = args.LATMIN
#print(lonmin, latmin, lonmax, latmin)
#print(dem_name)
bounds = [float(lonmin), float(latmin), float(lonmax), float(latmin)]
#print(bounds)
# %%

# if parser not working comment out parser section and just add dem name and bounds in below

#dem_name = 'glo_30'
#bounds = [-169.0, 53., -167.0, 54.]

# %%
# functions to create dem
def tag_dem_xml_as_ellipsoidal(dem_path: Path) -> str:
    xml_path = str(dem_path) + '.xml'
    assert(Path(xml_path).exists())
    tree = etree.parse(xml_path)
    root = tree.getroot()

    y = etree.Element("property", name='reference')
    etree.SubElement(y, "value").text = "WGS84"
    etree.SubElement(y, "doc").text = "Geodetic datum"

    root.insert(0, y)
    with open(xml_path, 'wb') as file:
        file.write(etree.tostring(root, pretty_print=True))
    return xml_path


def fix_image_xml(isce_raster_path: str) -> str:
    isce_apps_path = site.getsitepackages()[0] + '/isce/applications'
    fix_cmd = [f'{isce_apps_path}/fixImageXml.py',
               '-i',
               str(isce_raster_path),
               '--full']
    fix_cmd_line = ' '.join(fix_cmd)
    subprocess.check_call(fix_cmd_line, shell=True)
    return isce_raster_path


def download_dem_for_isce2(extent: list,
                           dem_name: str = 'glo_30',
                           dem_dir: Path = None,
                           buffer: float = .004) -> dict:
    """
    Parameters
    ----------
    extent : list
        [xmin, ymin, xmax, ymin] for epsg:4326 (i.e. (x, y) = (lon, lat))
    dem_name : str, optional
        See names in `dem_stitcher`
    full_res_dem_dir : Path, optional
    low_res_dem_dir : Path, optional
    buffer : float, optional
        In degrees, by default .001, which is .5 km at equator
    Returns
    -------
    Path
    """
    dem_dir = dem_dir or Path(f'{dem_name}')
    dem_dir.mkdir(exist_ok=True, parents=True)

    extent_geo = box(*extent)
    extent_buffered = list(extent_geo.buffer(buffer).bounds)
    extent_buffered = list(map(lambda e: round(e, 3), extent_buffered))

    dem_array, dem_profile = stitch_dem(extent_buffered,
                                        dem_name,
                                        dst_area_or_point='Point',
                                        dst_ellipsoidal_height=True,
                                        max_workers=5)

    full_res_dem_path = dem_dir/f'{dem_name}.dem.wgs84'
    dem_array[np.isnan(dem_array)] = 0.
    dem_profile['nodata'] = None
    dem_profile['driver'] = 'ISCE'
    with rasterio.open(full_res_dem_path, 'w', **dem_profile) as ds:
        ds.write(dem_array, 1)

    full_res_dem_xml = tag_dem_xml_as_ellipsoidal(full_res_dem_path)

    fix_image_xml(full_res_dem_xml)
    # lines 128 - 138 added by JH March 2022 - optional flag included to save out a tif copy for viewing.
    # if this is causing problems then delete if else loop (keep the return below as thats original)
    # if removing parser and adding in dem name and bounds directly in script this will need to be commented out as refs parser variable --gtif
    if args.gtif:
        print('-gtif flag used - saving geotiff copy')
        full_res_dem_gtif = dem_dir/f'{dem_name}.dem.wgs84.tif'
        # optional save out geotiff
        dem_profile['nodata'] = None
        dem_profile['driver'] = 'GTiff'
        with rasterio.open(full_res_dem_gtif, 'w', **dem_profile) as ds2:
            ds2.write(dem_array,1)
        print('Code Complete')
    else:
        print('Code Complete')


    return full_res_dem_xml

# %%
# change Path, dem_name etc. in the download_dem_for_isce2 function above
# default is that it puts the dem in the location where you are running the script in a subdir called isce_dem
download_dem_for_isce2(extent=bounds,
                       dem_name=dem_name,
                       dem_dir=Path('isce_dem'))

