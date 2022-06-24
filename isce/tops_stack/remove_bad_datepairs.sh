#!/bin/bash

#This script was written by Brie Corsa and Andy Monaghan on June 21, 2022
# Last editted by Brie Corsa on June 24, 2022

#If pairs_diff_starting_ranges.txt has date/image pairs listed, run this script before submit_runfiles_jobs_v3.sh



echo "REMOVING BAD DATEPAIR FROM RUN_FILES"
echo "May have to run this multiple times?"
 datepairs=$(grep _ pairs_diff_starting_ranges.txt)
 for datepair in $datepairs
 do
  grep -nR $datepair run_files/* |awk -F":" '{print $2 , $1}' >temp.txt

  numfiles=$(wc -l temp.txt | awk '{print $1}')
  for i in $(seq 1 $numfiles)
  do
   lineno=$(sed -n "${i}p" temp.txt | awk '{print $1}')
   filename=$(sed -n "${i}p" temp.txt | awk '{print $2}')
   sed -i -e "${lineno}d" ${filename}
  done

 done


#rm temp.txt
echo "MOVE ALL CONFIG FILES"

 mkdir moved_files_and_directories
 grep _ pairs_diff_starting_ranges.txt > new_temp.txt
 for f in $(cat new_temp.txt);
     do
     FILE=./configs/config_filtIon_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_generate_igram_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_generateIgram_ion_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_igram_filt_coh_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_igram_unw_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_merge_igram_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=./configs/config_misreg_$f
     if [ -f "$FILE" ]; then
         echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
 done


echo "MOVE OTHER CONFIG FILES"
 for f in $(cat new_temp.txt);
     do
     read date1 date2 <<< $( echo $f | awk -F"_" '{print $1" "$2}' )
     echo $date1
     echo $date2 
     FILE=./configs/config_look_ion_$date1-$date2
     echo $FILE
     if [ -f "$FILE" ]; then
       echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=configs/config_mergeBurstsIon_${date1}-${date2}
     if [ -f "$FILE" ]; then
       echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
     FILE=configs/config_unwrap_ion_${date1}-${date2}
     if [ -f "$FILE" ]; then
       echo "$FILE exists moving into moved_files_and_directories"
         mv $FILE ./moved_files_and_directories
     else
         echo "$FILE does not exist."
     fi
 done


rm new_temp.txt
rm temp.txt   
