#!/usr/bin/env python

import os
from PIL import Image
from PIL.ExifTags import TAGS


def print_all_exif_tags():
    print('\n--- TAGS')
    for key, value in TAGS.items():
        print('    ' + str(key) + '---' + str(value))
    print('--- TAGS')


def get_labeled_exif(fileName):


    image = Image.open(fileName)
    exif_info = image._getexif()
    if exif_info is None:
        print("    No info!!!!!!!")
    else:
        for tag, value in exif_info.items():
            if ('Model' == TAGS.get(tag)) :
                print('    Model: ' + str(value))






def analyzeSingleFile(fileName, outFile):
    """ Analyzes a single file
    """
    print("FileName: " + fileName)

    img = Image.open(fileName)
    outFile.write('test: ' + fileName + '\n')
    outFile.write('\n\n')

    exif_info_labled = get_labeled_exif(fileName)





# Reads the file and process it line by line
print('')
fileList = open('out_dir/fileList.txt')
outputFile = open('out_dir/fileData.txt', 'w')
for line in fileList:
    analyzeSingleFile(line[:-1], outputFile)

fileList.close()
outputFile.close()

#print_all_exif_tags()
print('--- Python done')



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
