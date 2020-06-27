#!/bin/bash
#--------------------------------------------------------
# Searches for double copies of images.
#--------------------------------------------------------
# Parameter: seach path
#            if empty using the one specified in the script
#            in SEACH_PATH.
#--------------------------------------------------------

# SEARCH_PATH default definion
#SEARCH_PATH=/volume1/photo
SEARCH_PATH=/volume1
#SEARCH_PATH=sampleImg

OUT_DIR=out_dir
FILE_LIST=${OUT_DIR}/fileList.txt

pushd . > /dev/null
ScriptDirectory=$(dirname $0)
cd "$ScriptDirectory"

echo "--- Parameter handling"
if [ 1 -eq $# ] ; then
    SEARCH_PATH=$1
fi

echo "--- Cleanup and prepare"
rm -rf  ${OUT_DIR}
mkdir -p ${OUT_DIR}

echo "--- Search all jpg and jpeg"
find ${SEARCH_PATH} -iname "*.jpeg" > ${FILE_LIST}
find ${SEARCH_PATH} -iname "*.jpg" >> ${FILE_LIST}

echo "--- Remove pics out of scope, e.g. e-mail box"
cp "${FILE_LIST}" "${FILE_LIST}.all"
cat "${FILE_LIST}" | \
    grep -v "^/volume1/photo/all/" | \
    grep -v "^/volume1/Reto/Mail/" | \
    grep -v "^/volume1/zSync/DataReto/MailBackup/" | \
    grep -v "^/volume1/Reto/mailBackup/" | \
    grep -v "^/volume1/@docker/" | \
    grep -v "/iTunes/iTunes Music/" | \
    grep -v "@eaDir" > ${FILE_LIST}.2
mv ${FILE_LIST}.2 ${FILE_LIST}


echo "--- Python Info"
which python3
python3 --version

echo "--- Get picture properties"
#python3 -d -v findDoublesAdv.py
python3 findDoublesAdv.py

echo "--- done"

# Return to the original directory
popd > /dev/null
