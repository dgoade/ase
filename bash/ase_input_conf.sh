#!/bin/bash
# Automation Scripting Essential Skills 
# Bash

# Input: Reading configuration files

config="${1:-./ase.conf}"
name="${2:-setting1}"

echo "======================="
logMsg="First technique -- source the file and use eval with escaped quote for assignment"
unset value
. ${config}
eval value=\${${name}}
echo "${logMsg}"
echo "value=${value}"


echo "======================="
logMsg="Second technique -- use grep and cut"
unset value
value="$(grep "^${name}=" $config|cut -d= -f2)"
echo "${logMsg}"
echo "value=${value}"

echo "======================="
logMsg="Third technique -- change the IFS built-in, redirect conf file to stdin and use 'read'"
unset value
echo "${logMsg}"

CUR_IFS=${IFS}
IFS="="
while read key value 
do
    if [ ${key} = "${name}" ]
    then
        IFS=${CUR_IFS}
        eval ${key}=${value}
        IFS="="
        break
    fi
done < ${config}
IFS=${CUR_IFS}
echo "value=${value}"
