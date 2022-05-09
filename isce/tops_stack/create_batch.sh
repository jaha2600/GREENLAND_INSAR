#!/bin/bash
### Jasmine Hansen 2022 ###
# compile all shell scripts together and add the && symbol at the end to run all together

ls run* > batch.sh

# add the symbol to the end.

sed -i 's/$/\ \&\&/' batch.sh

#add the ./ to start of each line
sed -i 's/^/\.\//' batch.sh

#then need to remove && from the end of the file 

sed -i 's/run_16_unwrap \&\&/run_16_unwrap/' batch.sh

# give permissions to all shell scripts
chmod +x *

