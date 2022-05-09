# MintPy on RMACC Summit

These codes faciliate the installation and submission of jobs on HPC systems (specifically RMACC Summit)

More details on the main software package can be found here: Miami INsar Time-series software in PYthon (MintPy) https://github.com/insarlab/MintPy

Main contributors: Jasmine Hansen (jasmine.hansen@colorado.edu)

## Installation
Run the `mintpy_summit_install.sh` script on an scompile node to install mintpy and associated dependencies onto summit. 

USER CHANGES: user must replace `KEY` in line 25 with their personal CDS key.

## Batch Job Submission
Set up your directory structure and `.cfg` file as per instructions on MintPy github page (https://github.com/insarlab/MintPy).

I would reccomend including the dask parallel options which speeds up the running of the algorithm (see MintPy info.)

Copy script `sbatch_mintpy.sh` to dir with `.cfg` file in it and submit on scompile node `sbatch sbatch_mintpy.sh`

USER CHANGES: user must change `.cfg` file name on line 22 of `sbatch_mintpy.sh` to match name of actual file in directory.

ISSUES: Jasmine currently gets a gdal error when running mintpy with GACOS corrections instead of the default ERA. Still being looked into but user may be able to fix by adding the following modules to top of `sbatch_mintpy.sh`

`ml intel/17.4`


`ml gdal/3.4.2`

## Other Scripts
Example config files with varying mintpy parameters 

Misc scripts for visualizing and converting formats of data. 

### If code used in publication please reference this github, mintpy, and the associated authors listed in each script.