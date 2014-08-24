#!/usr/bin/python


# Automation Scripting Essential Skills 
# Python

# Input: Parsing command-line parameters 
# Technique1 -- Use getopt 
import getopt
import sys

def usage():
    print "usage"

def main():

    rval = True

    help = False
    logLevel = "error"
    no_op = False
    verbose = False
 
    try:
        opts, args = getopt.getopt(sys.argv[1:], "a:hl:nv", ["action=", "help", "loglevel=", "noop", "verbose"])
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        usage()
        rval = False

    if rval:
        no_op = False
        verbose = False
        for o, a in opts:
            if o in ("-a", "--action"):
                action = a
            elif o in ("-h", "--help"):
                help = True
                usage()
                rval = False
            elif o in ("-l", "--loglevel"):
                logLevel = a
            elif o in ("-n", "--noop"):
                no_op = True
            elif o in ("-v", "--verbose"):
                verbose = True
            else:
                assert False, "unhandled option"

    if rval:
        print "You passed these args:"
        print ("action: %s" % action)
        print ("help: %s" % help)
        print ("loglevel: %s" % logLevel)
        print ("noop: %s" % no_op)
        print ("verbose: %s" % verbose)

if __name__ == "__main__":
    main()
