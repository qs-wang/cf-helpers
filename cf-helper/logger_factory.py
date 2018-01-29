"""
Create a logger with format, loglevel and name
"""
import logging
import os

LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')

def create_logger(name):
    loglevel = os.getenv('LOG_LEVEL', 'info')
    level = get_log_level(loglevel.upper())
    logging.basicConfig(format=LOG_FORMAT)
    logger = logging.getLogger(__name__)
    logger.setLevel(level)
    return logger


def get_log_level(level_string):
    levels = {
        "DEBUG": logging.DEBUG,
        "INFO": logging.INFO,
        "WARNING": logging.WARNING,
        "CRITICAL": logging.CRITICAL
    }
    return levels[level_string]
