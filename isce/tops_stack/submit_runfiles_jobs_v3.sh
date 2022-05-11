#!/bin/sh
## Written by Andy Monaghan, Joel Johnson & Jasmine Hansen ##
## May 9th 2022 JH edit to manually add --ntasks and add max stage numbers

### Below are job lengths for a 10 interferogram test set (still running at present).
# run_01 - 24 ntasks - 44 min, run_02 - 12 ntasks - 46 sec, run_03 - 12 ntasks - 15 sec, run_04 - 12 ntasks - 10 sec, run_05 - 12 ntasks - 25 min
# run_06 - 12 ntasks - 50 min, run_07 - 12 ntasks - 55 min, run_08 - 12 ntasks - 10 sec, run_09 - 12 ntasks - 03 hrs, run_10 - 12 ntasks - 01 hr 14 min
# run_11 - 12 ntasks - 02 min, run_12 - 12 ntasks - 04 hrs, run_13 - 12 ntasks - 14 min, run_14, run_15, run_16 - 12 ntasks - MEM FAIL

##### experimental - add the prep stage into the start and make the run_01 stage dependent on that job and then continue as normal #####
# submit prep stage (needs to be in same dir as submit_runfiles script)
#i=0
#id=`sbatch --export=NONE --partition=shas --qos=normal --account= --job-name=prep_stage --output=prep_output_%j.out --nodes=1 --ntasks=6 --time=24:00:00 prep_stack_par.sh | awk '{print $4}'`
#echo "submitted prep stage as $id with 6 ntasks"

# now submit the run_01 with the added dependency of the prep stage needing to run first
 #i=1
 #EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 #NUM_TASKS=24
 #id2=$id
 #id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 #echo "submitted initial job $EXE_SCRIPT as $id with $NUM_TASKS ntasks, which depends on job $id2"


 i=1
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=24

 id=`sbatch --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submitted initial job $EXE_SCRIPT as $id with $NUM_TASKS ntasks"
 i=2
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=3
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=4
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=5
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=6
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=7
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=8
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=9
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=10
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=11
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=12
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=13
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=14
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=15
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=16
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=17
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=18
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=19
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=20
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2" 
 
 i=21
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=22
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=23
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"

 i=24
 EXE_SCRIPT=$(sed -n "${i}p" run_files/run_list)
 NUM_TASKS=12
 id2=$id
 id=`sbatch --depend=afterok:$id2 --export=NONE --partition=shas --qos=normal --account= --job-name=${EXE_SCRIPT} --output=${EXE_SCRIPT}_output_%j.out --nodes=1 --ntasks=${NUM_TASKS} --time=24:00:00 ./runfiles_jobs.sh | awk '{print $4}'`
 echo "submited job $EXE_SCRIPT as $id with ${NUM_TASKS} ntasks, which depends on job $id2"
 
 
 