#!/usr/bin/env python

# Automation Scripting Essential Skills 
# Python

# Input: Parsing command-line parameters 
# Technique1 -- Use sys.argv array 
import sys

print ('You passed %s parameters.' % (len(sys.argv) -1) )

# slice into the array starting at 1 since element 
# zero is the name of this script
#for arg in  sys.argv[1:] :
#    print ('param: %s' % arg )

# since I want to list the arg #'s too
for ndx in range(1, len(sys.argv)) :
    print ('param# %s: %s' % (ndx, sys.argv[ndx]) )
