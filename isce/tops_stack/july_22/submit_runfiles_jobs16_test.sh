#!/bin/sh
## Written by Andy Monaghan, Joel Johnson & Jasmine Hansen ##
## JH edited to make pathing absolute - needs checking ##

WORK_DIR=/scratch/summit/$USER/GREENLAND

cd $WORK_DIR


# FOR EACH LINE IN THE RUN_FILES/RUN_LIST FILE submit an individual sbatch job 
# then - only once all of the run_16 parallel jobs have COMPLETED then start the next stage 

 i=16
 # uses i to extract the right line from the run_list list file
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24

# now read into the run_16 line file:
for line in $($EXE_SCRIPT) ; do
  # submit the line in the file as an individual sbatch job
  id=`sbatch --export=NONE --partition=shas --qos=normal --account=ucb62_summit3 --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./SUBMIT_LINES.sh | awk '{print $4}'`
  echo "submitted initial job $EXE_SCRIPT as $id with $NUM_TASKS ntasks"

; done 

# ISSUES I CAN FORSEE
# we need to submit each line from the run_16 shell script in its own shell script (equivalent in kind to runfiles_jobs.sh) because thats how we load the anaconda modules.
# so we can't just do the above command and change SUBMIT_LINES.sh to the python command from the line in the file.

# we could set it up like mikes SETSM script - where you run the prep_isce stage 
 
ml purge
ml gcc/10.2.0
ml gnu_parallel/20210322
ml anaconda
conda activate isce2

python run_16_line_1_file.py (or whatever the extracted line is)
