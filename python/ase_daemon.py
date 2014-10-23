#!/usr/bin/env python

# Automation Scripting Essential Skills 
# Python
# Daemon: How to daemonize a script

# Technique1 -- Python Daemonize: https://pypi.python.org/pypi/daemonize
# I tried Python Daemonize but it was taking me too long to understand it.

# Technique2 -- Use Sander Marechal's daemon3x class:
# http://www.jejik.com/articles/2007/02/a_simple_unix_linux_daemon_in_python/
# This is simple, elegant and exactly what I was looking for.

import sys, time
from daemon3x import daemon
import logging
import logging.config

LogFileName='./logging.log'
LogLevel='DEBUG'

class MyDaemon(daemon):
    def run(self):
	    while True:
		    time.sleep(5)
		    logger.debug('MyDaemon is running')

if __name__ == "__main__":

    logging.config.fileConfig('conf/ase_logging.conf')
    logger = logging.getLogger('root')

    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
	    if 'start' == sys.argv[1]:
		    logger.debug('Starting MyDaaemon')
		    daemon.start()
	    elif 'stop' == sys.argv[1]:
		    logger.debug('Stopping MyDaemon')
		    daemon.stop()
	    elif 'restart' == sys.argv[1]:
		    logger.debug('Restarting MyDaaemon')
		    daemon.restart()
	    else:
		    print "Unknown command"
		    sys.exit(2)
	    sys.exit(0)
    else:
	    print "usage: %s start|stop|restart" % sys.argv[0]
	    sys.exit(2)

