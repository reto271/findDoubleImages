#!/usr/bin/env python

import os
import csv
import operator
from functools import reduce
from enum import IntEnum
#from datetime import datetime

DATA_FILE_LOCATION = './out_dir/'
INPUT_FILE = 'fileDataClean.csv'
RESULT_FILE = 'sortedData.'
DOUBLE_LIST_FILE = 'doublePicsList.'
OUT_FILE_EXTENSION = 'csv'

class PictureProperties(IntEnum):
    Model            = 0
    DateTimeOriginal = 1
    ExifImageWidth   = 2
    ExifImageHeight  = 3
    FileName         = 4
    Directory        = 5
    FileSize         = 6



def numericalWithEmpty(val):
    if ('' == val):
        returnValue = 0
    else:
        returnValue = val
    return int(returnValue)


def writeFile(fileName, header, dataList):
    # Write the sorted data to the output file
    with open(fileName, 'w') as csvFile:
        csvwriter = csv.writer(csvFile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header)
        for row in dataList:
            csvwriter.writerow(row)
    csvFile.close()


''' IMPORTANT:
    The sorted list must be sorted according the parameters used to find doubles. There is no search and compare
     only adjacent rows are compared.
'''
def findDoubles(sortedList):
    # Keep if similar files (model, time, file size, pic dimensions)
    doubleList=[]
    for a, b in zip(sortedList, sortedList[1:]):
        if ((a[PictureProperties.Model.value] == b[PictureProperties.Model.value]) and
            (a[PictureProperties.DateTimeOriginal.value] == b[PictureProperties.DateTimeOriginal.value]) and
            (a[PictureProperties.FileSize.value] == b[PictureProperties.FileSize.value])):
            a.append(b[PictureProperties.Directory.value])
            a.append(b[PictureProperties.FileName.value])
            doubleList.append(a)

    # Write the sorted data to the output file
    header.append('Path Double')
    header.append('ImageName Double')
    return doubleList

with open(DATA_FILE_LOCATION + INPUT_FILE) as inputFile:
    dataList = csv.reader(inputFile, delimiter=';')
    header = next(dataList)
    sortedList=dataList

    # Define sort order
    sortedList = sorted(sortedList, key=lambda row: (row[PictureProperties.FileName.value]))
    sortedList = sorted(sortedList, key=lambda row: (numericalWithEmpty(row[PictureProperties.ExifImageWidth.value])))
    sortedList = sorted(sortedList, key=lambda row: (numericalWithEmpty(row[PictureProperties.ExifImageHeight.value])))
    sortedList = sorted(sortedList, key=lambda row: (int(row[PictureProperties.FileSize.value])))
    sortedList = sorted(sortedList, key=lambda row: (row[PictureProperties.DateTimeOriginal.value]))
    sortedList = sorted(sortedList, key=lambda row: (row[PictureProperties.Model.value]))
    #sortedList = sorted(sortedList, key=lambda row: (row[PictureProperties.Directory.value]))

    # Write the sorted data to the output file
    writeFile(DATA_FILE_LOCATION + RESULT_FILE + OUT_FILE_EXTENSION, header, sortedList)

    dblList = sortedList
    dblList = findDoubles(dblList)

    writeFile(DATA_FILE_LOCATION + DOUBLE_LIST_FILE + OUT_FILE_EXTENSION, header, dblList)

inputFile.close()
