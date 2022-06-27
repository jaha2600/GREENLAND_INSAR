# ISCE2 on RMACC Summit
Scripts to build and then submit jobs for stackSentinel.py from the ISCE2 project on summit.

Main contributors: Jasmine Hansen (jasmine.hansen@colorado.edu), Joel Johnson (joel.johnson@colorado.edu), and Andy Monaghan (CU Reseach Computing)
## Installation
Check if you have the following directory:

`/projects/$USER/software/anaconda/`

If you do - then copy the `isce2install.sh` into `/projects/$USER/software/` and execute it as detailed below.

If you do NOT - then follow the following instructions taken from [this site](https://curc.readthedocs.io/en/latest/software/python.html#configuring-conda-with-condarc)

Open your `.condarc` file in your favorite text editor (e.g., nano, vim):  
> _Note: this file may not exist yet -- if not, just create a new file with this name; you can open or create file with the following command_

```
[johndoe@shas0137]$ nano ~/.condarc
```

...and paste the following four lines:
```
pkgs_dirs:
  - /projects/$USER/.conda_pkgs
envs_dirs:
  - /projects/$USER/software/anaconda/envs
```
Once you have followed the instructions in that section check that you now have `/projects/$USER/software/anaconda/` and continue with installation instructions.

Place `isce2install.sh` and the file `isce2.yml` in the same directory as one another.

Run the `isce2install.sh` script on an scompile node to install isce2 and associated dependencies onto summit. It also adds the correct paths to your .bashrc file

USER CHANGES: user needs to add their earthdata username and password on line 44 to allow automated download of orbit files.
Once installed you should be able (on scompile) to run ml anaconda, conda activate isce2, and be able to check stackSentinel.py executes correctly with no inputs.

## Batch Job Submission
On sbatch use `summit_stack.sh` to run. This generates run files via stackSentinel.py and then executes them using in a batch shell script. It is set up for use with the ionospheric correction module so user will have to edit script to remove these. See https://github.com/isce-framework/isce2/tree/main/contrib/stack/topsStack.

You will likely have to resubmit this job a few times due to the 24 hr max timeout window for shas nodes. If you look in the slurm output file it will tell you the stage where the script timed out. Remove the completed run_file lines from the `batch.sh` script in the run_files directory and resubmit the script commenting out everything but `cd run_files` and `./batch.sh` lines.

USER CHANGES: upper and lower bounds for ion selection (line 26); dem, bounding box etc. for stackSentinel.py command.

USER TROUBLESHOOTING: delete the orbits directory before starting another run to avoid errors (it will automatically re-download them when running stackSeninel.py), make sure you've changed path in dem xml file

`create_batch.sh` and `create_batch_ion.sh` are standalone bash scripts that can be used to batch execute run file directories in normal and ion stack runs. Mostly for use on personal machines.

## Batch Parallel Job Submission
Developed with CU Reseach Computing - Andy Monaghan 

STILL IN TESTING

This submits each run stage as a seperate sbatch submission and uses GNU parallel to speed up stages. 

### Step 1
Run sbatch for script `prep_stack_par.sh` in main isce2 directory which runs the stackSentinel script to create all run files. This is currently set up for ionopsheric correction runs (see topsStack github for more info.)

I WOULD STRONGLY RECCOMEND DELETING YOUR ORBITS DIRECTORY EACH TIME YOU DO A NEW RUN / RERUN YOUR PREP SCRIPT

USER CHANGES: match to your desired ion and stackSentinel.py commands (check if you need the -p flag as you do for Greenland by may not for other areas), bounds, slurm parameters and check directory names.

### Step 2
Navigate to main isce stack directory. Place `runfile_jobs.sh` and `submit_runfiles_jobs_v3.sh` in directory.

Submit `./submit_runfiles_jobs_v3.sh` in commandline - not using sbatch command but ensure you are on an scompile node.

USER CHANGES: check `--account`, `--nodes` and other associated slurm commands. Check number of stages is equal to number of run_file changes in the directory. For each stage change `$NUM_TASKS` to match what you want it to be. Some information about jobtime vs ntasks can be found in the top of the script. 

File Variations:

There a few variations of the submit_runfiles and runfiles_jobs scripts in the directory which are mostly related to trying to find the most optimum balance between job speed and scheduling. Below I outline what the differences are:

`submit_runfiles_jobs_abs.sh` This is a version of submit_runfiles_jobs that can be run from your /projects/$USER directory, you place the path to the isce stack directory at the top. It has to copy runfiles_jobs.sh into the isce stack directory as that cannot be absolutely pathed.

`submit_runfiles_jobs_total.sh` This hasn't been tested yet but it just integrates the prep_stack_par.sh stage into the bulk submission of jobs. Again place prep_stack_par.sh in the isce stack directory. Run_files stage 01 should then run upon successful completion of this stage.

`runfiles_jobs_2.sh` This uses two cpus per task for GNU parallel to improve memory when running computationally heavy stages. This may end up being the default runfiles_jobs script. Using two cpus per task ONLY works if --ntasks is equal to or less than 12. If you do use this script remember to change the name in the submit_runfiles script. 

### If code used in publication please reference this github, isce2, and the associated authors listed in each script.