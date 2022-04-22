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

ml purge
ml gcc/10.2.0
ml anaconda
conda activate mintpy

# usage = sbatch sbatch_mintpy.sh Kanger_test.txt (infile is the config file)
INFILE=$1

smallbaselineApp.py INFILE