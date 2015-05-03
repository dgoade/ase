#!/usr/bin/env python

__author__ = 'dgoade'


# Automation Scripting Essential Skills
# Python

# Output: Logging
# Technique2 -- Use python2.7's core logging and configDict with yaml
import sys
import yaml
import logging
from logging.config import dictConfig
from pprint import pformat

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

    if rval:
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warn('This is a warn message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

if __name__ == "__main__":
    main()
