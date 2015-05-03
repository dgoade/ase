#!/usr/bin/env python


# Automation Scripting Essential Skills 
# Python

# Input: Reading configuration files
# Technique1 -- Use ConfigParser and an ini-type file 
import sys
import ConfigParser

# SafeConfigParser supports interpolation
config = ConfigParser.SafeConfigParser()
config.read(sys.argv[1])

print config.get('root', sys.argv[2])
