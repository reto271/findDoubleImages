ll#!/bin/bash

# Change to the script dir
pushd . > /dev/null
ScriptDirectory=$(dirname $0)
cd "$ScriptDirectory"/out_dir

cat fileInfoList.txt | sort -n > fileList01.txt
cat fileList01.txt | grep -v "/volume1/zuniPics/all/" > fileList02.txt

cat fileList02.txt | grep "SYNOPHOTO_THUMB_PREVIEW.jpg" > fileList03_syno1.txt
cat fileList02.txt | grep "SYNOPHOTO_THUMB_S.jpg" > fileList03_syno2.txt
cat fileList02.txt | grep "SYNOPHOTO:THUMB_S.jpg" > fileList03_syno3.txt
cat fileList02.txt | \
    grep -v "SYNOPHOTO_THUMB_PREVIEW.jpg" | \
    grep -v "SYNOPHOTO_THUMB_S.jpg" | \
    grep -v "SYNOPHOTO:THUMB_S.jpg" > fileList03_noSyno.txt

# fileList04 manually deleted some pics
# cat fileList04_manual.txt | grep -v "@eaDir" > fileList05.txt
cat fileList03_noSyno.txt | grep -v "@eaDir" > fileList05.txt

#

# Return to the original directory
popd > /dev/null
