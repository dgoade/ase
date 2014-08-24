#!/bin/bash
# Automation Scripting Essential Skills 
# Bash

# Input: Getting command line paramaters

echo "======================="
logMsg="First technique -- positional args"

OPTS=$@

echo "${logMsg}"
echo "args: $OPTS"
echo "Number of args: $#"

ndx=1
for arg in ${OPTS}
do
    echo "arg #${ndx} = ${arg}"
    let "ndx+=1"
done    
