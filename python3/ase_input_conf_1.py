#!/usr/bin/env python3


# Automation Scripting Essential Skills 
# Python

# Input: Reading configuration files
# Technique1 -- Use ConfigParser and an ini-type file 
import sys
import configparser

# SafeConfigParser supports interpolation
config = configparser.ConfigParser()
config.read(sys.argv[1])

print(config.get('root', sys.argv[2]))
