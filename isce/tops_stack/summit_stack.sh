#!/bin/bash

# Written by: Jasmine Hansen jaha2600@colorado.edu
# Purpose: This script submits a job on RMACC Summit. Can be used with other HPC systems if SBATCH/scheduling commands are changed.   
#SBATCH --account=      # Summit allocation
#SBATCH --partition=shas    # Summit partition
#SBATCH --qos=                # Summit qos
#SBATCH --time=24:00:00           # Max wall time
#SBATCH --nodes=1          # Number of Nodes
#SBATCH --ntasks=24          # Number of tasks per job

#SBATCH --job-name=sstack      # Job submission name
#SBATCH --mail-type=END            # Email user when job finishes
#SBATCH --mail-user=jaha2600@colorado.edu # Email address of user

# purge existing modules
ml purge
# load modules
ml gcc/10.2.0
ml anaconda
conda activate isce2

# select files in correct places for ion corr
# add the correct upper and lower bounds for your dataset
s1_select_ion.py -dir ./slc -sn 65.505836/67.561638 -nr 10

#then run the stack senintel to make the run files 
# no need to have an orbits directory as it will download automatically
# need to have slc/ dem/ aux_dir/
stackSentinel.py -s slc/ -d dem/glo_30.dem.wgs84 -a aux_dir/ -o orbits/ -b '65.505836 67.561638 -55.494823 -49.108829' -c 4 -p hv --param_ion ./ion_param.txt --num_connections_ion 3

# move to runfiles directory
cd run_files/

# compile all shell scripts together and add the && symbol at the end to run all together - creates a bash script called batch.sh that you can then execute

# list individual run files
ls run* > batch.sh
# add the && symbol to the end.
sed -i 's/$/\ \&\&/' batch.sh
#add the ./ to start of each line
sed -i 's/^/\.\//' batch.sh
#then need to remove && from the end of the file 
sed -i 's/run_24_invertIon \&\&/run_24_invertIon/' batch.sh

### JH ADD AND HAS TESTED ON SUMMIT AND SEEMS TO WORK WELL ###
### adds echo commands to start an end of each run file to make it easier to see where we get to if fail / timeout 
ls run* > run_list
# add text to start of file so you know the section.
for f in $(cat run_list) ; do sed -i "1s/^/echo '${f} START'\n/" ${f}; done
# then add the ending text to end of script.
for i in $(cat run_list) ; do echo "echo '${i} END'" >> ${i} ; done 

# give permissions to all shell scripts
chmod +x *

# run batch script which executes the scripts in order one after the other
./batch.sh

echo 'Script Complete'