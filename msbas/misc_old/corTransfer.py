#!/usr/bin/env python3

import os
import glob
import shutil
import argparse

#get directory information.
def getparser():
    # Parser to submit inputs for scripts. See Jul 27 Email from Jasmine
    parser = argparse.ArgumentParser(description="Input equivalent of SETUP_DIR in your .sh script to find COR files. See positional arg for example")
    parser.add_argument('current_dir', type=str, help='home directory holding date pair folders. For example, add /net/tiampostorage2/volume2/JoelShare2/KristyProcessing/Colorado/Calwood/10m after calling this script')
    return parser

parser = getparser()
args = parser.parse_args()
currentdir= args.current_dir
os.chdir(currentdir)

dates = glob.glob('20*')
datesize =len(dates)
print(str(datesize) + " folders found")

savepath= os.path.join(currentdir, "CORfiles")

if os.path.isdir(savepath): 
	print("Transfer folder exists")
else: 
	os.mkdir(savepath) 
	print("making Transfer folder")

for i in range(datesize):

	#Go into dir to copy things from
	copyfromdir = os.path.join(currentdir,dates[i])
	print("copying from: " + copyfromdir)
	os.chdir(copyfromdir)


	logfilefrom=os.path.join(copyfromdir,"isce.log")
	print(logfilefrom)
	copyfrommerged = os.path.join(copyfromdir,'merged/')

	if os.path.isdir(copyfrommerged) and os.path.isfile(logfilefrom): #Confirm if ISCE ran, if so, copy isce.log

		#Make folders for copying into
		os.system("ls")
		#Copy all the COR preview files to a new directory.. 
		for file in glob.glob(r'S1-INSAR-*-COR*'):
			print(file)
			shutil.copy2(file,savepath)
	else:
		print("merged dir "+ copyfrommerged+ " does not exist")

print("COR files copied")