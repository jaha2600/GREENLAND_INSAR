#!/usr/bin/env python3

import os
import glob
import shutil

currentdir='/scratch/summit/jojo8550/Lagos/5m/desc'
os.chdir(currentdir)

# list the directories
dates = glob.glob('20*')
# list number of directories
datesize =len(dates)
print(str(datesize) + " folders found")

mergedfiles = 'filt_topophase.unw.geo', 'filt_topophase.unw.geo.vrt', 'filt_topophase.unw.geo.xml'
mergedsize=len(mergedfiles)
print(str(mergedsize) + " merged files to transfer")

savepath= os.path.join(currentdir, "MSBASformat")



for i in range(datesize):

	#Go into dir to copy things from
	copyfromdir = os.path.join(currentdir,dates[i])
	print(copyfromdir)
	os.chdir(copyfromdir)


	logfilefrom=os.path.join(copyfromdir,"isce.log")
	print(logfilefrom)
	copyfrommerged = os.path.join(copyfromdir,'merged/')

	if os.path.isdir(copyfrommerged) and os.path.isfile(logfilefrom): #Confirm if ISCE ran, if so, copy isce.log

		#Make folders for copying into
		copytodir = os.path.join(savepath,dates[i])
		os.mkdir(copytodir)

		#Using shutil.move() to copy isce.log
		os.system("ls")
		logfileto=os.path.join(copytodir,"isce.log")
		shutil.copy2(logfilefrom, logfileto)

		#Move to merged to copy files there. 
		os.chdir(copyfrommerged)

		#Make folders and go into merged for files we need there. 
		copytomerged = os.path.join(copytodir,'merged')
		if os.path.isdir(copytomerged):
			print("merged destination exists")
		else: 
			os.mkdir(copytomerged)
			print("merged folder created")

		for j in range(mergedsize):
			print(j)
			movefilepath = os.path.join(copyfrommerged,mergedfiles[j])
			movefilesto = os.path.join(copytomerged, mergedfiles[j])

			print("checking following file: " + movefilepath)
	
			if os.path.isfile(movefilepath): 
				print(movefilepath + " exists")
				shutil.copy2(movefilepath,movefilesto)
	else:
		print("merged dir "+ copyfrommerged+ " does not exist")

print("relevant files now copied")