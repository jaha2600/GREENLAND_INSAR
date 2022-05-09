#!/bin/sh
## Written by Andy Monaghan, Joel Johnson & Jasmine Hansen ##
## May 9th 2022 JH edit to manually add --ntasks
 i=1
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 id=`sbatch --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=24 --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submitted initial job $EXE_SCRIPT as $id with 24 ntasks"

 i=2
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=24 --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with 24 ntasks, which depends on job $id2"

 i=3
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=24 --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with 24 ntasks, which depends on job $id2"

 i=4
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=24 --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with 24 ntasks, which depends on job $id2"