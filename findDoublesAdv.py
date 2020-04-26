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
        registered = False
        for key, value in TAGS.items():
            if (tagName == str(value)) :
                self.m_tagFilter.append(key)
                registered = True
        if (False == registered) :
            print('Tag not found: ' + tagName)

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
        line = line + ';FileName;Directory\n'
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
        try:
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
                line = line + ';' + os.path.basename(fileName)
                line = line + ';' + os.path.dirname(fileName)
                line = line[1:] + '\n'
                outFile.write(line)
        except IOError:
            print('FileName: ' + fileName + ' -> No valid file')
# --- end class PicturePropertyLogger -----------------------------------------------------------


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
logger.registerTag('DateTimeOriginal')    # 36867---DateTimeOriginal
#logger.registerTag('XResolution')    # 282---XResolution
#logger.registerTag('YResolution')    # 283---YResolution
#logger.registerTag('ImageWidth')    # 256---ImageWidth
#logger.registerTag('ImageLength')    # 257---ImageLength
#logger.registerTag('CellWidth')    #     264---CellWidth
#logger.registerTag('CellLength')    #     265---CellLength
#logger.registerTag('SMinSampleValue')
#logger.registerTag('RelatedImageWidth')
#logger.registerTag('RelatedImageLength')
logger.registerTag('ExifImageWidth')
logger.registerTag('ExifImageHeight')
#logger.registerTag('Make')
#logger.registerTag('Orientation')
logger.processFileList()

# Print all available tags
print_all_exif_tags('out_dir/availableProperties.txt')

print('--- Python done')
