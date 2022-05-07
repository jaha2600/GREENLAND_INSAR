# now submit sbatch runs for each run file, but make sure it holds the first one until the next
# parallize certain stages to speed up production.
WORKDIR='/scratch/summit/jaha2600/GREENLAND/2022/stack_mintpy/kanger_test_ion/'
mkdir ${WORKDIR}/logs/

## TO DO: ##
# 1. how to add conda activate isce2 into each of these sbatch commands? (required for running)
# 2. add hold to stage 2 onwards to hold sub until previous complete.
# 3. add parallization using GNU parallel to run_02 and many others.
##

sbatch --qos=normal --job-name=run_01 --account=ucb-summit-mjw --partition=shas --time=24:00:00 --nodes=1 --ntasks=10 --mail-type=END --mail-user=jaha2600@colorado.edu --error=${WORKDIR}/logs/run_01.err --output=${WORKDIR}/logs/run_01.out ${WORKDIR}/run_files/run_01_unpack_topo_reference

# --delay .2 prevents overloading the controlling node
# -j is the number of tasks parallel runs so we set it to 24 (the number of steps we want to run)
# --joblog makes parallel create a log of tasks that it has already run
# --resume makes parallel use the joblog to resume from where it has left off
# the combination of --joblog and --resume allow jobs to be resubmitted if necessary and continue from where they left off
# --a submit each line in this file as sep 

parallel --delay .2 -j $SLURM_NTASKS --joblog ${WORKDIR}/logs/par_run_02.log --resume -a ${WORKDIR}/run_02_unpack_secondary_slc
# lifted from RMACC guide
#my_parallel="parallel --delay .2 -j $SLURM_NTASKS"
##my_srun="srun --export=all --exclusive -n1 --cpus-per-task=1 --cpu-bind=cores"
#$my_parallel "$my_srun ./run_02_......" ::: {1..20}

# below add flag to not submit until run_01 complete. also add parallel  
sbatch --qos=normal --job-name=run_02 --account=ucb-summit-mjw --partition=shas --time=24:00:00 --nodes=1 --ntasks=10 --mail-type=END --mail-user=jaha2600@colorado.edu --error=${WORKDIR}/logs/run_02.err --output=${WORKDIR}/logs/run_02.out PARALLEL STEP ${WORKDIR}/run_files/run_02_unpack_secondary_slc

# add below for each stage depending par / no parallel.

#load balance
# shas testing for prep script 