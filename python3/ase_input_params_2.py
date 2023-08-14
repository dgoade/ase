#!/usr/bin/env python3

# Automation Scripting Essential Skills 
# Python

# Input: Parsing command-line parameters 
# Technique2 -- Use getopt
import getopt
import sys


def usage():
    print("usage")


def main():

    result = True

    help = False
    log_level = "error"
    no_op = False
    verbose = False
 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:hl:nv", ["action=", "help", "loglevel=", "noop", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print(str(err)) # will print something like "option -a not recognized"
        usage()
        result = False

    if result:
        action = 'run'
        no_op = False
        verbose = False
        for o, a in opts:
            if o in ("-a", "--action"):
                action = a
            elif o in ("-h", "--help"):
                help = True
                usage()
                result = False
            elif o in ("-l", "--loglevel"):
                log_level = a
            elif o in ("-n", "--noop"):
                no_op = True
            elif o in ("-v", "--verbose"):
                verbose = True
            else:
                assert False, "unhandled option"

    if result:
        print("You passed these args:")
        print(f"action: {action}")
        print(f"help: {help}")
        print(f"loglevel: {log_level}")
        print(f"noop: {no_op}")
        print(f"verbose: {verbose}")


if __name__ == "__main__":
    main()
