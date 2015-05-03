#!/usr/bin/env python

__author__ = 'david.goade'


# Automation Scripting Essential Skills
# Python

# Output: Logging
# Technique2 -- Use python2.7's core logging and configDict with yaml
import sys
import yaml
import logging
from logging.config import dictConfig
from pprint import pformat

LogFileName='./logging.log'
LogLevel='DEBUG'
Verbose=True

def main():

    rval=True

    f = open(sys.argv[1])
    config_dict = yaml.safe_load(f)
    f.close()

    if config_dict:
        dictConfig(config_dict['logging'])
    else:
        pass

    logger = logging.getLogger('Main.{0}'.format(__name__))
    log_msg = 'Logging config dictionary loaded successfully.'
    logger.debug(log_msg)

    logger.debug('Logging pformatted data of the config_dict')
    logger.debug(pformat(config_dict))

    if Verbose:
        # Add the console handler
        ch = logging.StreamHandler()
        ch.setLevel(1)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)


    if rval:
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warn('This is a warn message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

if __name__ == "__main__":
    main()
