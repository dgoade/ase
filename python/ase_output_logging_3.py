#!/usr/bin/env python

__author__ = 'dgoade'


# Automation Scripting Essential Skills
# Python

# Output: Logging
# Technique3 -- Use python's core logging and configDict with yaml
import sys
import yaml
import logging
from logging.config import dictConfig
from pprint import pformat


class Configurator:

    config_dict = {
        "setting1": "foo",
        "setting2": "bar",
        "setting3": "baz",
        "logging": {
          "version": 1,
          "formatters": {
              "simple": {
                  "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                  }
              },
          "handlers": {
              "console": {
                  "class": "logging.StreamHandler",
                  "level": "DEBUG",
                  "formatter": "simple",
                  "stream": "ext://sys.stdout"
                },
              "stderr": {
                 "class": "logging.StreamHandler",
                 "level": "WARN",
                 "formatter": "simple",
                 "stream": "ext://sys.stderr"
                },
            "file": {
              "class": "logging.FileHandler",
              "formatter": "simple",
              "filename": "ase_output_logging_3.log"
              }
            },
          "loggers": {
            "__main__": {
              "level": "DEBUG",
              "handlers": [
                "file",
                "console"
                ],
              "propagate": "no"
              }
            },
          "root": {
            "level": "WARNING",
            "handlers": [
            ]
          }
        }
      }


def main():

    rval=True

    configurator = Configurator()
    if configurator.config_dict['logging']:
        print('configuring logging from dict')
        dictConfig(configurator.config_dict['logging'])
    else:
        pass

    logger = logging.getLogger(__name__)
    log_msg = 'Logging config dictionary loaded successfully.'
    logger.debug(log_msg)
    logger.debug('Logging pformatted data of the config_dict')
    logger.debug(pformat(configurator.config_dict))

    if rval:
        logger.debug('This is a debug message')
        logger.info('This is an info message')
        logger.warn('This is a warn message')
        logger.error('This is an error message')
        logger.critical('This is a critical message')

if __name__ == "__main__":
    main()
