#!/usr/bin/env python

import os
from PIL import Image
from PIL.ExifTags import TAGS


class PicturePropertyLogger:
    m_picFileList = None
    m_outFile = None
    m_tagFilter = []

    def setPictureFileList(self, picFileList, outFile):
        self.m_picFileList = picFileList
        self.m_outFile = outFile

    def registerTag(self, tagName):
        for key, value in TAGS.items():
            if (tagName == str(value)) :
                self.m_tagFilter.append(key)

    def processFileList(self):
        if (None == self.m_picFileList):
            print('No list file registered')
        else:
            if (0 == len(self.m_tagFilter)):
                print('No tags registered')
            else:
               self. __processFileList()

    def __processFileList(self):
        fileList = open(self.m_picFileList)
        outputFile = open(self.m_outFile, 'w')

        # Add header line to file
        line = ''
        for logTag in self.m_tagFilter:
            tagName =  TAGS.get(logTag)
            if (0 == len(line)):
                line = tagName
            else:
                line = line + ';' + tagName
        line = line + '\n'
        outputFile.write(line)

        # Process all files
        for line in fileList:
            self.__analyzeSingleFile(line[:-1], outputFile)

        # Cleanup
        fileList.close()
        outputFile.close()


    def __analyzeSingleFile(self, fileName, outFile):
        """ Analyzes a single file
        """
        image = Image.open(fileName)
        exif_info = image._getexif()
        if exif_info is None:
            print('FileName: ' + fileName + ' -> No info')
        else:
            line = ''
            for logTag in self.m_tagFilter:
                tagFound = False
                for tag, value in exif_info.items():
                    if (logTag == tag) :
                        # print(str(TAGS.get(logTag)) + '  : ' + str(value))
                        line = line + ';' + str(value)
                        tagFound = True
                if (False == tagFound) :
                    line = line + ';'
            line = line[1:] + '\n'
            outFile.write(line)


''' Prints all available tags in the exif structure '''
def print_all_exif_tags(tagFileName):
    outputFile = open(tagFileName, 'w')
    outputFile.write('Available exif - TAGS\n')
    for key, value in TAGS.items():
        outputFile.write('    ' + str(key) + '---' + str(value) + '\n')
    outputFile.close()



# Reads the file and process it line by line
logger = PicturePropertyLogger()
logger.setPictureFileList('out_dir/fileList.txt', 'out_dir/fileData.csv')
logger.registerTag('Model')
logger.registerTag('DateTime')            # 306---DateTime
logger.registerTag('DateTimeOriginal')    # 36867---DateTimeOriginal
logger.registerTag('DateTimeDigitized')   # 36868---DateTimeDigitized
logger.registerTag('PreviewDateTime')     # 50971---PreviewDateTime

logger.processFileList()

# Print all available tags
print_all_exif_tags('out_dir/availableProperties.txt')

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
