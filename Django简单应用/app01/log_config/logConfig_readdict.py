import json
import logging
import logging.config
import os

import yaml

def create_mylogger (default_path="logconfig.json", default_level=logging.DEBUG):
    path = default_path
    if os.path.exists(path):
        with open(path, "r") as f:
            config = json.load(f)
            logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)
    return logging.getLogger('simple_logger')

if __name__ == '__main__':
    logger = create_mylogger()
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')