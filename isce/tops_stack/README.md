# ISC2 on RMACC Summit
Scripts to build and then submit jobs for stackSentinel.py from the ISCE2 project on summit
## Installation
Run the `isce2install.sh` script on an scompile node to install isce2 and associated dependencies onto summit. It also adds the correct paths to your .bashrc file
USER CHANGES: user needs to add their earthdata username and password on line 44 to allow automated download of orbit files.
Once installed you should be able (on scompile) to run ml anaconda, conda activate isce2, and be able to check stackSentinel.py executes correctly with no inputs.

## Batch job submission
On sbatch use `summit_stack.sh` to run. This generates run files via stackSentinel.py and then executes them using in a batch shell script. It is set up for use with the ionospheric correction module so user will have to edit script to remove these. See https://github.com/isce-framework/isce2/tree/main/contrib/stack/topsStack.
USER CHANGES: upper and lower bounds for ion selection (line 26); dem, bounding box etc. for stackSentinel.py command.

USER TROUBLESHOOTING: delete the orbits directory before starting another run to avoid errors (it will automatically re-download them when running stackSeninel.py), make sure you've changed path in dem xml file

`create_batch.sh` and `create_batch_ion.sh` are standalone bash scripts that can be used to batch execute run file directories in normal and ion stack runs. Mostly for use on personal machines.

Things that I think would be useful to add:

Its likely some jobs would timeout on summit. So instead of running from start some way to know which run*.sh it failed and then you can just manually resubmit the remaining scripts / slice off the top of the batch.sh. 