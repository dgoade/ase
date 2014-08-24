#!/bin/bash
# Automation Scripting Essential Skills 
# Bash

# Input: Getting command line paramaters

echo "======================="
logMsg="Second technique -- using getopts"

OPTS=$@

HELP=0
NO_OP=0
VERBOSE=0

OPTIND=1
while getopts a:hl:nv option ${OPTS}
do
    case ${option} in
        a) ACTION="${OPTARG}"
        ;;
        h) HELP=1
        ;;
        l) LOG_LEVEL="${OPTARG}"
        ;;
        n) NO_OP=1
        ;;
        v) VERBOSE=1
        ;;
        *) 
        ;;
    esac
done    
shift $(($OPTIND - 1)) 

echo "${logMsg}"
echo "ACTION=${ACTION}"
echo "HELP=${HELP}"
echo "LOG_LEVEL=${LOG_LEVEL}"
echo "NO_OP=${NO_OP}"
echo "VERBOSE=${VERBOSE}"
