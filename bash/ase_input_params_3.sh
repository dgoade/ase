#!/bin/bash
# Automation Scripting Essential Skills 
# Bash

# Input: Getting command line paramaters
echo "======================="
logMsg="Third technique -- combine positional args and emulate getoptslong"
echo "${logMsg}"
echo "args: ${@}"


get_option()
{    

    declare -i rval=0
    declare -i num_args=${1}
    declare -i ndx=${2}
    declare setting=${3}

    declare -i next_ndx
    declare next_arg

    if [ ${num_args} > ${ndx} ]
    then
        let "next_ndx=${ndx}+1"
        next_arg=${opt_array[${next_ndx}]}
        if [ ${next_arg:0:1} = "-" ]
        then
            : # don't assign
        else
            eval "${setting}=${next_arg}"
            rval=1
        fi
    fi

    return ${rval}

}

parse_args()
{

    declare -i rval=0
    declare -a opt_array=(${@})
    declare -i ndx=0
    declare -i skip_arg=0
    declare -i has_opts=0
    declare -i in_opts=0
    declare -i end_opts=0
    declare -i num_args=0
    declare arg
    declare errMsg

    let "num_args=${#opt_array[@]}-1"
    echo "Number of args: $(expr ${num_args} + 1)"

    for ndx in $(seq 0 ${num_args})
    do

        if [ ${skip_arg} -eq 1 ]
        then
            skip_arg=0
        else
            arg=${opt_array[${ndx}]}
            echo "arg #${ndx} = ${arg}"

            if [ ${arg:0:1} = "-" ]
            then
                if [ ${end_opts} -eq 1 ]
                then
                    echo "No options allowed after --"
                    in_opts=0
                    rval=1
                else
                    in_opts=1
                    has_opts=1
                fi
            else
                in_opts=0
            fi

            if [ ${rval} -eq 0 ]
            then
                if [ ${in_opts} -eq 0 ]
                then
                    if [ ${has_opts} -eq 1 ]
                    then
                        if [ ${end_opts} -eq 1 ]
                        then
                            : 
                            # this arg is not preceded with a '-' but the arg
                            # before it was '--',  which means this and all 
                            # following args will be parsed positionally
                        else
                            errMsg="Positional args must follow '--'" 
                            errMsg="${errMsg} when options are included."
                            echo ${errMsg}
                            rval=1
                        fi
                    else
                        : # there were not any '-' options on the command line
                    fi
                    if [ ${rval} -eq 0 ]
                    then
                        # here is where you assign variables positionally
                        ACTION=${arg}
                    fi
                else
                    case "${arg}" in
                        --) 
                            end_opts=1
                        ;;
                        -a|--action) 
                            get_option ${num_args} ${ndx} ACTION
                            skip_arg=${?}
                        ;;
                        -h|--help) 
                            HELP=1
                        ;;
                        -l|--loglevel) 
                            get_option ${num_args} ${ndx} LOG_LEVEL
                            skip_arg=${?}
                        ;;
                        -n|--noop) 
                            NO_OP=1
                        ;;
                        -v|--verbose) 
                            VERBOSE=1
                        ;;
                        *) 
                            echo "Invalid option: ${arg}"
                            rval=1
                        ;;
                    esac
                fi # [ ${in_opts} -eq 0 ]
            fi # [ ${rval} -eq 0 ]
        fi # [ ${skip_arg} -eq 1 ]
    done

    return ${rval}

}

parse_args $@
rval=${?}
if [ ${rval} -eq 0 ]
then 
    echo "Arguments parsed successfully"
else
    echo "Failed to parse arguments"
fi
echo "ACTION=${ACTION}"
echo "HELP=${HELP}"
echo "LOG_LEVEL=${LOG_LEVEL}"
echo "NO_OP=${NO_OP}"
echo "VERBOSE=${VERBOSE}"
