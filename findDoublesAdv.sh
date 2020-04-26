#!/bin/bash
#--------------------------------------------------------
# Searches for double copies of images.
#--------------------------------------------------------
# Parameter: seach path
#            if empty using the one specified in the script
#            in SEACH_PATH.
#--------------------------------------------------------

# SEARCH_PATH default definion
#SEARCH_PATH=/home/reto/Pictures
#SEARCH_PATH=/home/reto/Pictures/2012/20120512_SpielenStattEssen
SEARCH_PATH=sampleImg
OUT_DIR=out_dir
FILE_LIST=${OUT_DIR}/fileList.txt
FILE_INFO_LIST=${OUT_DIR}/fileInfoList.txt

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

echo "--- Find all jpg and jpeg"
find ${SEARCH_PATH} -iname "*.jpeg" > ${FILE_LIST}
find ${SEARCH_PATH} -iname "*.jpg" >> ${FILE_LIST}

echo "--- Remove pics out of scope, e.g. e-mail box"
cat "${FILE_LIST}" | grep -v "/volume1/Reto/Mail/V2/" | grep -v "/volume1/zbkMac_01/mailBackup" > ${FILE_LIST}.2
mv ${FILE_LIST}.2 ${FILE_LIST}


echo "--- Python Info"
which python3
python3 --version

echo "--- Analyze Files"
#python3 -d -v findDoublesAdv.py
python3 findDoublesAdv.py

echo "--- done"

popd > /dev/null
