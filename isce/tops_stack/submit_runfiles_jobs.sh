#!/bin/sh

numsteps=4

for i in `seq 1 ${numsteps}`; do
 #Find script that corresponds to index
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 #Find out how many lines to run in script (for parallelization)
   #Note max is total number of cores on node (24 for Summit "shas")
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))

    if [ $i == 1 ]; then
     id=`sbatch --export=NONE --partition=shas --qos=normal --account=ucb-summit-mjw --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=$NUM_TASKS --time=01:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
     echo "submitted initial job $id with $NUM_TASKS ntasks"
   else
    id2=$id
     id=`sbatch --depend=afterany:$id --export=NONE --partition=shas --qos=normal --account=ucb-summit-mjw --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=$NUM_TASKS --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
    echo "submited job $id with $NUM_TASKS ntasks, which depends on job $id2"
   fi
done