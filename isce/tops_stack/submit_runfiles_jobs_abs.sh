#!/bin/sh
## Written by Andy Monaghan, Joel Johnson & Jasmine Hansen ##
## JH edited to make pathing absolute - needs checking ##

WORK_DIR=/scratch/summit/$USER/GREENLAND

cd $WORK_DIR

# copy the runfile_jobs.sh script to the $WORK_DIR directory if its not already there as that is relative pathed and cannot be run from /projects.

RUNFILE=/projects/$USER/..../runfiles_jobs.sh 

if [[ -f "$RUNFILE" ]]; then
  echo "$RUNFILE already exists"
else
  cp $RUNFILE $WORK_DIR
  echo "$RUNFILE copied to $WORK_DIR"
fi


 i=1
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24

 id=`sbatch --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submitted initial job $EXE_SCRIPT as $id with $NUM_TASKS ntasks"

 i=2
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=3
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=4
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=5
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=6
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=7
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=8
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=9
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=10
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=11
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=12
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=13
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=14
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=15
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=16
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=17
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=18
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=19
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=20
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=$(wc -l run_files/${EXE_SCRIPT} | awk '{print $1}')
 NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=21
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=22
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=23
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=24
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24
 id2=$id
 id=`sbatch --depend=afterany:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"
 
 
 