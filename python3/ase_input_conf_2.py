#!/usr/bin/env python

# Automation Scripting Essential Skills 
# Python

# Input: Reading configuration files
# Technique2 -- Use yaml
import sys
import yaml

f = open(sys.argv[1])
dataMap = yaml.safe_load(f)
f.close()

print(dataMap[sys.argv[2]])
