#!/bin/bash
#--------------------------------------------------------
# Searches for double copies of images.
#--------------------------------------------------------
# Parameter: seach path
#            if empty using the one specified in the script
#            in SEACH_PATH.
#--------------------------------------------------------

# Change into the script directory
SCRIPTDIR=$(readlink -f $(dirname "$0"))
pushd "${SCRIPTDIR}" > /dev/null
pwd

feedback=0

echo "--- Remove all non-ascii chars"
tr -dC '[:print:]\t\n' < out_dir/fileData.csv > out_dir/fileDataClean.csv

echo "--- Python Info"
which python3
python3 --version

echo "--- Analyze Files"
python3 analyzeFilesAdv.py

echo "--- done"

# Return to the original directory
popd > /dev/null

exit ${feedback}
