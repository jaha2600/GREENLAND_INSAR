#!/bin/bash
#get the jobfile line and then run parallel 

# get specific params for this job
ls run* > run_list
numsteps=24

for i in `seq 1 ${numsteps}`; do
 #Find script that corresponds to index
  EXE_SCRIPT=$(sed -n "${i}p" run_list)
 #Find out how many lines to run in script (for parallelization)
   #Note max is total number of cores on node (24 for Summit "shas")
  NUM_TASKS=$(wc -l ${EXE_SCRIPT} | awk '{print $1}')
  NUM_TASKS=$(echo $((NUM_TASKS<24 ? NUM_TASKS : 24)))
 
  echo starting ${WORKFILE}
  parallel --jobs 20 < ${EXE_SCRIPT}
  echo finished ${WORKFILE}

done 