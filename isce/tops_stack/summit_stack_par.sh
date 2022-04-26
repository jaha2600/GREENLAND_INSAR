#!/bin/bash

# Written by: jaha2600@colorado.edu
# Date: 20220421
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
# load GNU parallel
ml parallel
conda activate isce2


# have individual sbatch submissions for each run file, that don't start until the first one has been executed

# within that you want to paralleize each line in the run file script so that it runs them all together