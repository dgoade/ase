#!/bin/bash
# Automation Scripting Essential Skills 
# Bash

# Output: Logging 

LogLevel="${1:-1}"

# String manipulation to get a log
# file named after this script.
BaseName=$(basename ${0:-${0}})
LogFile="${BaseName%.*}.log"

logIt()
{

    declare -i rval=0
    declare msgLogLevel="${1}"
    declare msg="${2}"

    declare dateFormat="+%Y-%m-%d %H:%M:%S"
    declare date=$(date "${dateFormat}")

    declare logMsg
    declare logFile

    if [ ${msgLogLevel} -ge ${LogLevel:-0} ]
    then
        msg=${2}
        logMsg="${date}|${msgLogLevel}|${BASH_LINENO[0]}|${msg}"
        logFile=${3:-${LogFile:-${/dev/null}}}

        # First technique -- using echo
        #echo "${logMsg}" | tee -a ${logFile}

        # Second technique -- using printf 
        printf "%s\n" "${logMsg}" | tee -a ${logFile}

        rval=$?
    else
        :
    fi

    return ${rval}
        
}

logIt 1 "This is logging at level 1"
logIt 2 "This is logging at level 2"
logIt 3 "This is logging at level 3"
logIt 4 "This is logging at level 4"
