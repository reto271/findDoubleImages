#!/bin/bash

# Change to the script dir
pushd . > /dev/null
ScriptDirectory=$(dirname $0)

rm -rf results
rm -rf temp
mkdir -p results
mkdir -p temp


cat out_dir/fileInfoList.txt | sort -n > temp/fileInfoList01.txt

# Remove unused
cat temp/fileInfoList01.txt | grep -v "@eaDir" > temp/fileInfoList02.txt
cat temp/fileInfoList02.txt | grep -v "/volume1/photo/all/" > temp/fileInfoList03.txt



# Finalize - find doubles
cp temp/fileInfoList03.txt results/fileInfoFinal01.txt

touch results/fileInfoFinal02_human.txt
touch results/fileInfoFinal02_machine.txt

OLD_SIZE=0
while read LINE ; do
    SIZE=$(echo ${LINE}      | awk -F"#" '{ print $1 }')
    DIM=$(echo ${LINE}       | awk -F"#" '{ print $2 }')
    NAME=$(echo ${LINE}      | awk -F"#" '{ print $3 }')
    NAME_PATH=$(echo ${LINE} | awk -F"#" '{ print $4 }')

    if [ ${SIZE} -eq ${OLD_SIZE} ] ; then
        # Human readable
        echo "${NAME} # ${SIZE} # ${DIM} # ${OLD_NAME} # ${OLD_DIM}" >> results/fileInfoFinal02_human.txt
        echo "   ${NAME_PATH}" >> results/fileInfoFinal02_human.txt
        echo "   ${OLD_NAME_PATH}" >> results/fileInfoFinal02_human.txt
        #Machine readable
        echo "${NAME} # ${SIZE} # ${NAME_PATH} # ${OLD_NAME_PATH} # ${DIM} # ${OLD_NAME} # ${OLD_DIM}" >> results/fileInfoFinal02_machine.txt
    fi
    OLD_SIZE=${SIZE}
    OLD_DIM=${DIM}
    OLD_NAME=${NAME}
    OLD_NAME_PATH=${NAME_PATH}

done < results/fileInfoFinal01.txt

cat results/fileInfoFinal02_machine.txt | sort > results/fileInfoFinal02_machine_sort.txt
#mv results/fileInfoFinal02_machine_sort.txt results/fileInfoFinal02_machine.txt


# Return to the original directory
popd > /dev/null

echo "Done"
