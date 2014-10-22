#!/usr/bin/env python

import logging 
import logging.config
from fabric.api import hide,local,env,settings,warn_only

LogFileName='./ase_exec.log'
LogLevel='DEBUG'
Verbose=True

def exec_script(script_name, script_opts):

    '''
    a good template
    function for general-purpose automation tasks
    that require executing an external shell script
    using fabric and capturing the stdout and stderr
    while keeping them separate.
    '''

    rval = 0
    logger = logging.getLogger('{0}.exec_script'.format(__name__))

    com='{0} "{1}"'.format(
        script_name,
        script_opts)

    logger = logging.getLogger('{0}.exec_script'.format(__name__))
    log_msg = 'Running external shell script: {0}'.format(script_name)

    try:
        with hide('everything'):
            proc=local(com, capture=True)
            logger.debug('return_code={0}'.format(proc.return_code))

            if proc.return_code == 0:
                log_msg = 'Script executed successfully: {0}'
                log_msg = log_msg.format(com)
                logger.debug(log_msg)
                rval = proc.return_code
            else:
                log_msg = 'Script execution failed: {0}'
                log_msg = log_msg = format(com)
                logger.error(log_msg)

        rval = proc.return_code

    except Exception:
        log_msg = "Exception occurred execute script"
        logger.exception(log_msg)
        rval = 1

    if( rval == 0 ):
        if( logger.isEnabledFor('DEBUG') ):
            if( proc.stdout ):
                log_msg = "--stdout from external script follows:\n{0}"
                log_msg = log_msg.format(proc.stdout)
                logger.debug(log_msg)
            if( proc.stderr ):
                log_msg = "--stderr from external script follows:\n{0}"
                log_msg = log_msg.format(proc.stderr)
                logger.debug(log_msg)
    else:
        if( proc.stdout ):
            log_msg = "--stdout from external script follows:\n{0}"
            log_msg = log_msg.format(proc.stdout)
            logger.error(log_msg)
        if( proc.stderr ):
            log_msg = "--stderr from external script follows:\n{0}"
            log_msg = log_msg.format(proc.stderr)
            logger.error(log_msg)

    return rval

def main():

    logging.config.fileConfig('conf/ase_logging.conf')
    logger = logging.getLogger('root')

    if Verbose:
        # Add the console handler
        ch = logging.StreamHandler()
        ch.setLevel(1)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        ch.setFormatter(formatter)
        logger.addHandler(ch)

    exec_script('ls', '-l')    

if __name__ == "__main__": main()
