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
SEARCH_PATH=/volume1
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

echo "--- Loop and determine size and properties"
while read FILE ; do
    #echo "File: ${FILE}"
    FILENAME=$(basename -- "${FILE}")
    ACTUAL_FILE_SIZE=$(du -b "${FILE}" | cut -f 1)
    #echo "ACTUAL_FILE_SIZE: ${ACTUAL_FILE_SIZE}"

    PIC_SIZE=$(identify -format "%wx%h\n" "${FILE}")
    #echo "PIC_SIZE: ${PIC_SIZE}"

    echo "${ACTUAL_FILE_SIZE} # ${PIC_SIZE} # ${FILENAME} # ${FILE}" >> ${FILE_INFO_LIST}
done < ${FILE_LIST}

echo "--- done"

popd > /dev/null
