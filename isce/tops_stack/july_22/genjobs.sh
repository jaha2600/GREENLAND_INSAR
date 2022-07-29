#!/bin/bash

#script to make template file from each dem in directory
#scheduling code

## This code only looks for one core to do its job.
## Select one node
#SBATCH --nodes=1
## Select 1 core for the job.
#SBATCH --ntasks=1
## Set shas (summit haswell) partition
#SBATCH --partition=shas
#SBATCH --account ucb-summit-mjw
## Set a time limit or walltime of 2 hours - it should be quick for small job lists.
#SBATCH --time=2:00:00

module load intel/17.4
#module load gcc/6.1.0
module load gdal/2.2.1
# I load geos
module load geos/3.6.2
# I load proj.
module load proj/4.9.2
# I load python
module load python/2.7.11

#script to make template file from each dem in directory

#scheduling code
## This code only looks for one core to do its job.
#makes uer the path to genjobs.input file matches your own - change usename at minimum.

run_16_shell_location='/ath/to/runfile/dir/run_16_unwrap'
#read in template file
template_file='/projects/jaha2600/demcoregister/template_file.txt'
user=`id -u -n`
#build jobfile directory
jobfile_directory="/path/to/where/want/individual/jobfiles/run_16_jobfiles/"
    if [ ! -d "$jobfile_directory" ]; then mkdir -p "$jobfile_directory"; fi

# example of a line : SentinelWrapper.py -c /gpfs/summit/scratch/jaha2600/GREENLAND/2022/stack_mintpy/kanger_25_365/configs/config_igram_unw_20180612_20180624
    
#for each pointcloud file do this
for command in $(cat run_16_shell_location) ; do
    #get unique id for file
    ids=${command%/*}
    jobfilename="run_16_${ids}.sh"
    cp $template_file $jobfilename

    #set parameters in the copied jobfilename
    #set the path at the top of script
    sed -i -e "s|COMMAND|${command}|g" $jobfilename

done < "$template_file"

echo "script complete" 
