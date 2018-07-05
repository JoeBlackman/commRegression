'''
************************************************************************************************************************
*File       statusLogger.py
*Author     Joseph Blackman
*Date       5/21/2018
*Brief      Python 3.6 module for managing status.log file
*           A module of the comm regression scripts package (ASCO P/N: 1258991)
*Source file Revision History
*
*Version 1.00
*   5/21/2018 JBLACKMAN
*       1. Initial Release
************************************************************************************************************************
'''

import logging as l
from logging import FileHandler as fh
from logging import StreamHandler as sh
from logging import Formatter as fmt

#def main(argv):
LOG_FORMAT = ('%(asctime)s [%(levelname)s]: %(message)s in %(pathname)s:%(lineno)d')
LOG_LEVEL = l.INFO
STATUS_LOG_FILE = 'status.log'

status_logger = l.getLogger('status')
status_logger.setLevel(LOG_LEVEL)
status_logger_file_handler = fh(STATUS_LOG_FILE)
status_logger_file_handler.setLevel(LOG_LEVEL)
status_logger_file_handler.setFormatter(fmt(LOG_FORMAT))
status_logger.addHandler(status_logger_file_handler)
status_logger_stream_handler = sh()
status_logger_stream_handler.setLevel(LOG_LEVEL)
status_logger_stream_handler.setFormatter(fmt(LOG_FORMAT))
status_logger.addHandler(status_logger_stream_handler)

#def getStatusLogger():
#    return l.getLogger('status')
#main(sys.argv[1:])