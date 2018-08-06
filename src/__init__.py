from os import path, remove
import logging

from config import LOG_FILE_NAME

if path.isfile(LOG_FILE_NAME):
    remove(LOG_FILE_NAME)

# Create the Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
 
# Create the Handler for logging data to a file
logger_handler = logging.FileHandler(LOG_FILE_NAME)
logger_handler.setLevel(logging.DEBUG)
 
# Create a Formatter for formatting the log messages
logger_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
 
# Add the Formatter to the Handler
logger_handler.setFormatter(logger_formatter)
 
# Add the Handler to the Logger
logger.addHandler(logger_handler)
logger.info('Completed configuring logger()!')
