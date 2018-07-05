'''
************************************************************************************************************************
*File       resultsLogger.py
*Author     Joseph Blackman
*Date       5/21/2018
*Brief      Python 3.6 module for managing results.csv file
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
from logging import Formatter as fmt

#def main(argv):
LOG_FORMAT = ('%(message)s')
LOG_LEVEL = l.INFO
RESULTS_LOG_FILE = 'results.csv'

results_logger = l.getLogger('results')
results_logger.setLevel(LOG_LEVEL)
results_file_handler = fh(RESULTS_LOG_FILE)
results_file_handler.setLevel(LOG_LEVEL)
results_file_handler.setFormatter(fmt(LOG_FORMAT))
results_logger.addHandler(results_file_handler)

# main(sys.argv[1:])