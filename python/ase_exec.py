#!/usr/bin/env python

"""
Automation Scripting Essential Skills (https://github.com/dgoade/ase)
Python

Execution: Execute an external command or script

Technique1 -- Use python2.7's core logging and configDict with yaml,
and fabric to execute an external command or shell script and
capture stdout and stderr separately

"""

import sys
import yaml
import logging
import re
from logging.config import dictConfig
from pprint import pformat
from fabric.api import hide,local,env,settings,warn_only

def execute(script_name, script_opts):

    rval = 0
    f = open(sys.argv[1])
    config_dict = yaml.safe_load(f)
    f.close()

    if config_dict:
        dictConfig(config_dict['logging'])
    else:
        pass

    logger = logging.getLogger('execute.{0}'.format(__name__))
    log_msg = 'Logging config dictionary loaded successfully.'
    logger.debug(log_msg)
    logger.debug('Logging pformatted data of the config_dict')
    logger.debug(pformat(config_dict))

    com='{0} "{1}"'.format(
        script_name,
        script_opts)

    log_msg = 'Running external command / script: {0}'.format(script_name)
    logger.debug(log_msg)

    try:
        with hide('everything'):
            proc=local(com, capture=True)
            logger.debug('return_code={0}'.format(proc.return_code))

            if proc.return_code == 0:
                log_msg = 'Executed successfully: {0}'
                log_msg = log_msg.format(com)
                logger.debug(log_msg)
                rval = proc.return_code
            else:
                log_msg = 'Execution failed: {0}'
                log_msg = log_msg.format(com)
                logger.error(log_msg)

        rval = proc.return_code

    except Exception:
        log_msg = "Exception occurred during execution"
        logger.exception(log_msg)
        rval = 1

    if( rval == 0 ):
        if( logger.isEnabledFor('DEBUG') ):
            if( proc.stdout ):
                log_msg = "--stdout from execution follows:\n{0}"
                log_msg = log_msg.format(proc.stdout)
                logger.debug(log_msg)
            if( proc.stderr ):
                log_msg = "--stderr from execution follows:\n{0}"
                log_msg = log_msg.format(proc.stderr)
                logger.debug(log_msg)
    else:
        if( proc.stdout ):
            log_msg = "--stdout from execution follows:\n{0}"
            log_msg = log_msg.format(proc.stdout)
            logger.error(log_msg)
        if( proc.stderr ):
            log_msg = "--stderr from execution follows:\n{0}"
            log_msg = log_msg.format(proc.stderr)
            logger.error(log_msg)

    return rval

def main():

    execute('ls', '-l')

if __name__ == "__main__": main()
