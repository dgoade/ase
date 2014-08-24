#!/usr/bin/python


# Automation Scripting Essential Skills 
# Python

# Input: Parsing command-line parameters 
# Technique1 -- Use logging 
import logging
import logging.config

LogFileName='./logging.log'
LogLevel='DEBUG'
Verbose=True

def main():

    rval=True

    logging.config.fileConfig('./logging.conf')
    logger = logging.getLogger('root')

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
