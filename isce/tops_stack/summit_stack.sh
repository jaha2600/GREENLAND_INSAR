#!/bin/bash

# Written by: jaha2600@colorado.edu
# Date: 20220421
# Purpose: This script submits a job on RMACC Summit. Can be used with other HPC systems if SBATCH/scheduling commands are changed.   
#SBATCH -A      # Summit allocation
#SBATCH --partition=shas    # Summit partition
#SBATCH --qos=                # Summit qos
#SBATCH --time=24:00           # Max wall time
#SBATCH --nodes=1          # Number of Nodes
#SBATCH --ntasks=24          # Number of tasks per job

#SBATCH --job-name=sstack-       # Job submission name
#SBATCH --mail-type=END            # Email user when job finishes
#SBATCH --mail-user=jaha2600@colorado.edu # Email address of user

# purge existing modules
module purge 
# load modules
module gcc/10.2.0 
module anaconda 
conda activate isce2 

# select files in correct places for ion corr
s1_select_ion.py -dir ./slc -sn 65.505836/67.561638 -nr 10

#then run the stack senintel to make the run files 
stackSentinel.py -s slc/ -d dem/glo_30.dem.wgs84 -a aux_dir/ -o orbits/ -b '65.505836 67.561638 -55.494823 -49.108829' -c 4 -p hv --param_ion ./ion_param.txt --num_connections_ion 3

cd run_files/

# compile all shell scripts together and add the && symbol at the end to run all together - creates a bash script called batch.sh that you can then execute

ls run* > batch.sh
# add the symbol to the end.
sed -i 's/$/\ \&\&/' batch.sh
#add the ./ to start of each line
sed -i 's/^/\.\//' batch.sh
#then need to remove && from the end of the file 
sed -i 's/run_24_invertIon \&\&/run_24_invertIon/' batch.sh
# try and insert the step number between each line
#get number of lines in batch file 
lines=$(cat batch.sh | wc -l)
for f in lines; do
sed -i '${f}i This is Line ${f}' batch.sh
done
# give permissions to all shell scripts
chmod +x *

# run batch script which executes the scripts in order one after the other
./batch.sh 

echo 'Script Complete'