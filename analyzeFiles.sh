#!/bin/bash

# Change to the script dir
pushd . > /dev/null
ScriptDirectory=$(dirname $0)
cd "$ScriptDirectory"/out_dir

cat fileInfoList.txt | sort -n > fileInfoList01.txt

# Remove unused
cat fileInfoList01.txt | grep -v "@eaDir" > fileInfoList02.txt
cat fileInfoList02.txt | grep -v "/volume1/photo/all/" > fileInfoList03.txt


# Finalize - find doubles
cp fileInfoList03.txt fileInfoFinal01.txt

rm fileInfoFinal02.txt
touch fileInfoFinal02.txt

while read line ; do
    #SIZE=$(cat ${line} | awk '{ print $1 }')

#      if ( ${SIZE} -eq ${SIZE_OLD} ) ; then
    echo "${line}" >> fileInfoFinal02.txt
#          echo "${SIZE}" >> fileInfoFinal02.txt
#          echo "${LINE_OLD}" >> fileInfoFinal02.txt
#          echo "---" >> fileInfoFinal02.txt
#      fi
#      LINE_OLD=${LINE}
#      SIZE_OLD=${SIZE}

done < fileInfoFinal01.txt


# Return to the original directory
popd > /dev/null
