#!/bin/bash

WORKDIR=$1
mkdir ${WORKDIR}/logs

ml purge
ml gcc/10.2.0
ml anaconda
conda activate isce2

# submit a job for each run file 
sbatch --qos=normal --account=ucb-summit-mjw --partition=shas --time=24:00:00 --nodes=1 --ntasks=10 --mail-type=END --mail-user=jaha2600@colorado.edu --error=${WORKDIR}/logs/job.err --output=${WORKDIR}/logs/job.out ${WORKDIR}/run_files/run_01_unpack_topo_reference

#thoughts:
#make everything hard coded vs realative path?
#check run time for different files from orirginal scripts from clayton
#edit/create parallel step thing
#or --wait instead of hold. 
# ./doParallelStep.sh