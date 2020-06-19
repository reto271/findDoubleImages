#!/usr/bin/env python

import os
import csv
import operator

#from datetime import datetime

DATA_FILE_LOCATION = './out_dir/'
INPUT_FILE = 'fileDataClean.csv'
RESULT_FILE = 'sortedData.csv'

with open(DATA_FILE_LOCATION + INPUT_FILE) as inputFile:
    dataList = csv.reader(inputFile, delimiter=';')
    header = next(dataList)
    sortedList=dataList

    # Define sort order
    sortedList = sorted(sortedList, key=lambda row: (row[4]))  # FileName
    sortedList = sorted(sortedList, key=lambda row: (row[0]))  # Model
    sortedList = sorted(sortedList, key=lambda row: (row[2]))  # ExifImageWidth
    sortedList = sorted(sortedList, key=lambda row: (row[3]))  # ExifImageHeight
    sortedList = sorted(sortedList, key=lambda row: (row[1]))  # DateTimeOriginal
    #sortedList = sorted(sortedList, key=lambda row: (row[4]))  # Directory


    with open(DATA_FILE_LOCATION + RESULT_FILE, 'w') as csvFile:
        csvwriter = csv.writer(csvFile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csvwriter.writerow(header)
        for row in sortedList:
            csvwriter.writerow(row)

csvFile.close()
inputFile.close()
