#!/usr/bin/env python

from PIL import Image



def get_exif(filename):
    image = Image.open(filename)
    image.verify()
    return image._getexif()

# exif = get_exif('sampleImg/P1010012_Panasonic.JPG')
# exif = get_exif('sampleImg/DSC_0157_NikonD5100.JPG')
# print(exif)




def analyzeSingleFile(fileName, outFile):
    """ Analyzes a single file
    """
    print("FileName: " + fileName)

    img = Image.open(fileName)
    outFile.write('test: ' + fileName + '\n')
    outFile.write('\n\n')

    exif_info = get_exif(fileName)
    print(exif_info)



# Reads the file and process it line by line
fileList = open('out_dir/fileList.txt')
outputFile = open('out_dir/fileData.txt', 'w')
for line in fileList:
    analyzeSingleFile(line[:-1], outputFile)

fileList.close()
outputFile.close()
print('--- Python done')



# #while read FILE ; do
# #    echo "File: ${FILE}"
# #    FILENAME=$(basename -- "${FILE}")
# #    ACTUAL_FILE_SIZE=$(du -b "${FILE}" | cut -f 1)
# #    #echo "ACTUAL_FILE_SIZE: ${ACTUAL_FILE_SIZE}"
# #
# #    # exif:Model: NIKON D5100
# #    # signature: 9d473e2c68ab78cc718deb2a06d7fae31d83e09fae812ef8c760ac012d701694
# #    # Geometry: 4928x3264+0+0
# #    # Resolution: 300x300
# #    # Print size: 16.4267x10.88
# #    MODEL=$(identify -verbose "${FILE}" | grep "exif:Model:")
# #    SIGNATURE=$(identify -verbose "${FILE}" | grep "signature:")
# #    GEOMETRY=$(identify -verbose "${FILE}" | grep "Geometry:")
# #    RESOLUTION=$(identify -verbose "${FILE}" | grep "^  Resolution:")
# #    IMG_SIZE=$(identify -verbose "${FILE}" | grep "Print size:")
# #
# #    MODEL=$(echo "${MODEL}" | awk -F": " '{ print $2 }')
# #    SIGNATURE=$(echo "${SIGNATURE}" | awk -F": " '{ print $2 }')
# #    GEOMETRY=$(echo "${GEOMETRY}" | awk -F": " '{ print $2 }')
# #    RESOLUTION=$(echo "${RESOLUTION}" | awk -F": " '{ print $2 }')
# #    IMG_SIZE=$(echo "${IMG_SIZE}" | awk -F": " '{ print $2 }')
# #
# #    # echo "MODEL      : ${MODEL}"
# #    # echo "SIGNATURE  : ${SIGNATURE}"
# #    # echo "GEOMETRY   : ${GEOMETRY}"
# #    # echo "RESOLUTION : ${RESOLUTION}"
# #    # echo "IMG_SIZE   : ${IMG_SIZE}"
# #
# #    echo "${FILENAME} # ${ACTUAL_FILE_SIZE} # ${SIGNATURE} # ${GEOMETRY} # ${RESOLUTION} # ${IMG_SIZE} # ${MODEL} # ${FILE}" | tee -a ${FILE_INFO_LIST}
# #done < ${FILE_LIST}
#
