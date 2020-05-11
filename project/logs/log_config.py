import json
import logging
import os

with open('config.json', 'r') as f:
    data = json.loads(f.read())
    LOG_DIR = data['logs']['path']
    LOG_FILE_DEBUG = data['logs']['debug']
    LOG_FILE_ERROR = data['logs']['error']
    LOG_FILE_GENERAL = data['logs']['general']

ENCODING = 'utf-8'


class InfoFilter(logging.Filter):
    def filter(self, rec):
        return rec.levelno == logging.INFO


logger = logging.getLogger('log')
logger.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh_debug = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE_DEBUG), encoding=ENCODING)
fh_debug.setLevel(logging.DEBUG)
# create file handler which logs even debug messages
fh_general = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE_GENERAL), encoding=ENCODING)
fh_general.addFilter(InfoFilter())
# create console handler with a higher log level
fh_error = logging.FileHandler(os.path.join(LOG_DIR, LOG_FILE_ERROR), encoding=ENCODING)
fh_error.setLevel(logging.WARNING)
# create console handler with a higher log level
sh = logging.StreamHandler()
sh.setLevel(logging.ERROR)
# create formatter and add it to the handlers
formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s: %(message)s")
fh_debug.setFormatter(formatter)
fh_general.setFormatter(formatter)
fh_error.setFormatter(formatter)
# add the handlers to logger
logger.addHandler(fh_debug)
logger.addHandler(fh_general)
logger.addHandler(fh_error)
