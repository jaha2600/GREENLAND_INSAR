#!/bin/bash

### Jasmine Hansen 2022 ###
# compile all shell scripts together and add the && symbol at the end to run all together

ls run* > batch.sh

# add the symbol to the end.

sed -i 's/$/\ \&\&/' batch.sh

#add the ./ to start of each line
sed -i 's/^/\.\//' batch.sh

#then need to remove && from the end of the file 

sed -i 's/run_24_invertIon \&\&/run_24_invertIon/' batch.sh

# try and insert the step number between each line
#get number of lines in batch file 
#lines=$(cat batch.sh | wc -l)
#for f in lines; do

#sed -i '${f}i This is Line ${f}' batch.sh

#done

# give permissions to all shell scripts
chmod +x *

