#!/usr/bin/env python

# Automation Scripting Essential Skills 
# Python

# Input: Parsing command-line parameters 
# Technique3 -- Use parsearg
import argparse


def usage():
    print("usage")

def main():

    result = True

    logLevel = "error"
    no_op = False
    verbose = False
 
    parser = argparse.ArgumentParser(description='Demonstrate how to parse command-line parameters')
    parser.add_argument("-a", "--action", help="the action to take")
    parser.add_argument("-l", "--loglevel", help="logging level")
    parser.add_argument("-n", "--noop", help="no-op or dry-run", action="store_true")
    parser.add_argument("-v", "--verbose", help="be verbose", action="store_true")
    args = parser.parse_args()

    if result:
        msg = """ You passed these args:
                   action: {}
                   loglevel: {}
                   noop: {}
                   verbose: {}""".format(args.action,
                                          args.loglevel,
                                          args.noop,
                                          args.verbose)
        print(msg)

if __name__ == "__main__":
    main()


