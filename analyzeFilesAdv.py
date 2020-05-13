#!/usr/bin/env python

import os
import csv
import operator

#from datetime import datetime

DATA_FILE_LOCATION = './out_dir/'
fileName = 'fileDataClean.csv'



print('hello')

#with open(DATA_FILE_LOCATION + fileName) as csvDataFile:
#    csvReader = csv.DictReader(csvDataFile)
#    cnt = 0
#    for row in csvReader:
#        if (cnt < 20):
#            print('cnt: ' + str(cnt))
#            print(row)
#            cnt = cnt + 1


with open('./TestData/test01.csv') as f:
    reader = csv.reader(f, delimiter=';')
    print('------------------------')
    for row in reader:
        print(row)

with open('./TestData/test01.csv') as f:
    reader = csv.DictReader(f, delimiter=';')
    print('------------------------')
    for row in reader:
        print(row['DateTimeOriginal'], row['ExifImageHeight'])

with open('./TestData/test01.csv') as f:
    reader = csv.reader(f, delimiter=';')
    print('------------------------')
    sortedList = sorted(reader, key=operator.itemgetter(2))
    for row in sortedList:
        print(row)
    print('------------------------')


with open('./TestData/test01.csv') as f:
    reader = csv.reader(f, delimiter=';')
    print('------------------------')
    scores = sorted(reader, key=lambda row: (row[1], row[0]))
    for row in scores:
        print(row)
    print('------------------------')
