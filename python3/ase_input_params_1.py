#!/usr/bin/env python3

# Automation Scripting Essential Skills 
# Python3

# Input: Parsing command-line parameters 
# Technique1 -- Use sys.argv array 
import sys

print(f"You passed {len(sys.argv) -1} parameters.")

# since I want to list the arg #'s too
for ndx in range(1, len(sys.argv)):
    print(f"param# {ndx}: {sys.argv[ndx]}")
