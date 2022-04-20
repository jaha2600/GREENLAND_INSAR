#!/bin/bash

#this script installs isce on Summit
#seperate scripts are needed because there are different gcc compilers on Summit than on Alpine

#load modules you need:
ml purge
ml gcc/10.2.0
ml cmake/3.14.1
ml anaconda

#create isce2 conda env w/ dependencies (5-10 min). Need if no conda isce2 env exists
conda create -y -n isce2 -c conda-forge python cython gdal git h5py libgdal pytest numpy fftw scipy basemap scons opencv

#activate the environment
conda activate isce2

#now go to your software directory:
cd /projects/$USER/software/anaconda

#now get and compile isce2
git clone https://github.com/isce-framework/isce2.git
mv isce2 isce2_summit
cd isce2_summit
export ISCE_BASE_DIR=$PWD
mkdir local
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=${ISCE_BASE_DIR}/local -DCMAKE_PREFIX_PATH=${CONDA_PREFIX}
make -j 8 install

#to run add these lines to your job script:

echo ml purge
echo ml gcc/10.2.0
echo ml anaconda
echo conda activate isce2
echo export ISCE_BASE_DIR=/projects/$USER/software/anaconda/isce2_summit
echo export PATH=${ISCE_BASE_DIR}/local/bin:${ISCE_BASE_DIR}/applications:$PATH
echo export PYTHONPATH=${ISCE_BASE_DIR}/local/packages:$PYTHONPATH

#I think we need to go to this /projects/jojo8550/software/anaconda/isce2/contrib/stack/topsStack/:$PATH
