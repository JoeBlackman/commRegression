'''
************************************************************************************************************************
*File       RDCanOpenWrapper.py
*Author     Joseph Blackman
*Date       5/21/2018
*Brief      Python 3.6 module for calling canopensocket processes from the RDCanOpenFolder in this package
*           A module of the comm regression scripts package (ASCO P/N: 1258991)
*Source file Revision History
*
*Version 1.00
*   5/21/2018 JBLACKMAN
*       1. Initial Release
************************************************************************************************************************
'''

import subprocess
from pathlib import Path
from subprocess import Popen, PIPE

#----------------------------------------------------------------------------------------------------------------------
#Function: call canopencomm on linux machine, print stdout to terminal
def callcanopencomm(nodeID, readWrite, index, subindex, datatype, writeValue = None):
    dirname = Path.cwd()
    filename = str(dirname / 'RDCanOpen/canopencomm')
    if writeValue is None:
        command = [filename, nodeID, readWrite, index, subindex, datatype]
    elif '-' in writeValue: #error here
        command = [filename, nodeID, readWrite, index, subindex, datatype, '--', writeValue]
    else:
        command = [filename, nodeID, readWrite, index, subindex, datatype, writeValue]
    try:
        process = Popen(command, stdout=PIPE, stderr=PIPE)
        stdout, stderr = process.communicate()
        return stdout, stderr
    except TimeoutError:
        process.kill()
        stdout, stderr = process.communicate()
        return stdout, stderr
    except Exception as e:
        return '', repr(e)
#----------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------
#Function: call initCanOpen.sh on linux machine
def canReset():
    subprocess.call(['/opt/RDCanOpen/initCanOpen.sh'], shell=False)
#----------------------------------------------------------------------------------------------------------------------
