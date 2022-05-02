# now submit sbatch runs for each run file, but make sure it holds the first one until the next
# parallize certain stages to speed up production.
cd /scratch/summit/jaha2600/GREENLAND/2022/stack_mintpy/kanger_test_ion/
mkdir logs/
### TO ADD: HOW TO ENSURE run_02.sh etc. DOES NOT SUBMIT UNTIL run_01 totally complete ###
### How to added parallelization on particular scripts ###
sbatch run_01.sh 
sbatch run_02.sh -- add flag to not submit until run_01.sh is done 
sbatch run_03.sh
sbatch run_04.sh
sbatch run_05.sh
sbatch run_06.sh
sbatch run_07.sh
sbatch run_08.sh
sbatch run_09.sh
sbatch run_10.sh
sbatch run_11.sh
sbatch run_13.sh
sbatch run_14.sh
sbatch run_15.sh
sbatch run_16.sh
sbatch run_17.sh
sbatch run_18.sh
sbatch run_19.sh
sbatch run_20.sh
sbatch run_21.sh
sbatch run_22.sh
sbatch run_23.sh
sbatch run_24.sh