# ISCE2 on RMACC Summit
Scripts to build and then submit jobs for stackSentinel.py from the ISCE2 project on summit.

Main contributors: Jasmine Hansen (jasmine.hansen@colorado.edu), Joel Johnson (joel.johnson@colorado.edu), and Andy Monaghan (CU Reseach Computing)
## Installation
Run the `isce2install.sh` script on an scompile node to install isce2 and associated dependencies onto summit. It also adds the correct paths to your .bashrc file

USER CHANGES: user needs to add their earthdata username and password on line 44 to allow automated download of orbit files.
Once installed you should be able (on scompile) to run ml anaconda, conda activate isce2, and be able to check stackSentinel.py executes correctly with no inputs.

## Batch Job Submission
On sbatch use `summit_stack.sh` to run. This generates run files via stackSentinel.py and then executes them using in a batch shell script. It is set up for use with the ionospheric correction module so user will have to edit script to remove these. See https://github.com/isce-framework/isce2/tree/main/contrib/stack/topsStack.

USER CHANGES: upper and lower bounds for ion selection (line 26); dem, bounding box etc. for stackSentinel.py command.

USER TROUBLESHOOTING: delete the orbits directory before starting another run to avoid errors (it will automatically re-download them when running stackSeninel.py), make sure you've changed path in dem xml file

`create_batch.sh` and `create_batch_ion.sh` are standalone bash scripts that can be used to batch execute run file directories in normal and ion stack runs. Mostly for use on personal machines.

## Batch Parallel Job Submission
Developed with CU Reseach Computing - Andy Monaghan 

STILL IN TESTING

This submits each run stage as a seperate sbatch submission and uses GNU parallel to speed up stages. 

### Step 1
Run sbatch for script `prep_stack_par.sh` in main isce2 directory which runs the stackSentinel script to create all run files. This is currently set up for ionopsheric correction runs (see topsStack github for more info.)

USER CHANGES: bounds, slurm parameters and check directory names.

### Step 2
Navigate to run_files directory. Place `runfile_jobs.sh` and `submit_runfiles_jobs.sh` in directory.

Submit `submit_runfiles_jobs.sh` in commandline - not using sbatch command but ensure you are on an scompile node.

USER CHANGES: check `--ntasks`, `--account`, `--nodes` and other associated slurm commands. Check number of stages is equal to number of run_file changes in the directory. 


### If code used in publication please reference this github, isce2, and the associated authors listed in each script.