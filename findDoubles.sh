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

# Parameter handling
if [ 1 -eq $# ] ; then
    SEARCH_PATH=$1
fi

# Cleanup and prepare
rm -rf  ${OUT_DIR}
mkdir -p ${OUT_DIR}

# Find all jpg and jpeg
find ${SEARCH_PATH} -iname "*.jpeg" > ${FILE_LIST}
find ${SEARCH_PATH} -iname "*.jpg" >> ${FILE_LIST}

# Remove pics out of scope, e.g. e-mail box
cat "${FILE_LIST}" | grep -v "/volume1/Reto/Mail/V2/" | grep -v "/volume1/zbkMac_01/mailBackup" > ${FILE_LIST}.2
mv ${FILE_LIST}.2 ${FILE_LIST}

# Loop and determine size and properties
while read FILE ; do
    echo "File: ${FILE}"
    FILENAME=$(basename -- "${FILE}")
    ACTUAL_FILE_SIZE=$(du -b "${FILE}" | cut -f 1)
    #echo "ACTUAL_FILE_SIZE: ${ACTUAL_FILE_SIZE}"

    # exif:Model: NIKON D5100
    # signature: 9d473e2c68ab78cc718deb2a06d7fae31d83e09fae812ef8c760ac012d701694
    # Geometry: 4928x3264+0+0
    # Resolution: 300x300
    # Print size: 16.4267x10.88
    MODEL=$(identify -verbose "${FILE}" | grep "exif:Model:")
    SIGNATURE=$(identify -verbose "${FILE}" | grep "signature:")
    GEOMETRY=$(identify -verbose "${FILE}" | grep "Geometry:")
    RESOLUTION=$(identify -verbose "${FILE}" | grep "^  Resolution:")
    IMG_SIZE=$(identify -verbose "${FILE}" | grep "Print size:")

    MODEL=$(echo "${MODEL}" | awk -F": " '{ print $2 }')
    SIGNATURE=$(echo "${SIGNATURE}" | awk -F": " '{ print $2 }')
    GEOMETRY=$(echo "${GEOMETRY}" | awk -F": " '{ print $2 }')
    RESOLUTION=$(echo "${RESOLUTION}" | awk -F": " '{ print $2 }')
    IMG_SIZE=$(echo "${IMG_SIZE}" | awk -F": " '{ print $2 }')

    # echo "MODEL      : ${MODEL}"
    # echo "SIGNATURE  : ${SIGNATURE}"
    # echo "GEOMETRY   : ${GEOMETRY}"
    # echo "RESOLUTION : ${RESOLUTION}"
    # echo "IMG_SIZE   : ${IMG_SIZE}"

    echo "${FILENAME} # ${ACTUAL_FILE_SIZE} # ${SIGNATURE} # ${GEOMETRY} # ${RESOLUTION} # ${IMG_SIZE} # ${MODEL} # ${FILE}" | tee -a ${FILE_INFO_LIST}
done < ${FILE_LIST}



popd > /dev/null
