'''
************************************************************************************************************************
*File       utilities.py
*Author     Joseph Blackman
*Date       5/21/2018
*Brief      Python 3.6 commonly used utilities used by modules in the comm regression scripts package
*           A module of the comm regression scripts package (ASCO P/N: 1258991)
*Source file Revision History
*
*Version 1.00
*   5/21/2018 JBLACKMAN
*       1. Initial Release
************************************************************************************************************************
'''

#built in modules
import unicodedata

#local modules

try:
    import unicodedata
except Exception as e:
    print(repr(e))

def findIndex(string, list):
    """Finds the index of a string in a list of strings, and returns it"""
    if string in list:
        for i in range(0, len(list)):
            element = list[i]
            if element == string:
                return i
    else:
        return None

def splitCANObject(CANObject):
    """Takes a string input, returns a list representation of the range represented by the string"""
    colonTokenIndex = CANObject.find(':')
    dashTokenIndex = CANObject.find('-')
    index = None
    subIndex = None
    if colonTokenIndex >= 0:
        #This is an index with a subindex
        index = CANObject[:colonTokenIndex]
        subIndex = CANObject[(colonTokenIndex + 1):]
    #elif dashTokenIndex >= 0:
    #    #This is a range of indicies, no sub-index
    #    indexStart = int(CANObject[:dashTokenIndex], 0)
    #    indexEnd = int(CANObject[(dashTokenIndex+1):], 0)
    #    for i in range(indexStart, (indexEnd+1)):
    #        index.append(hex(i))
    else:
        #This is an index without a subindex
        index = CANObject
        subIndex = '0x00'
    return (index, subIndex)

#for now, make a custom class, consider merging it with splitCANObject later
def splitModbusRegister(modbusRegister):
    """Takes a string input, returns a list representation of the range represented by the string"""
    colonTokenIndex = modbusRegister.find(':')
    dashTokenIndex = modbusRegister.find('-')
    register = None
    startBit = None
    bitwiseLength = None
    if colonTokenIndex >= 0:
        register = modbusRegister[:colonTokenIndex]
        if dashTokenIndex >=0:
            #this is a modbus register with a range of bits [ex: 40003:08-15]
            startBit = modbusRegister[(colonTokenIndex+1):dashTokenIndex]
            stopBit = modbusRegister[(dashTokenIndex + 1):]
            bitwiseLength = int(stopBit) - int(startBit) + 1
            bitwiseLength = str(bitwiseLength)
            startBit = str(startBit)
        else:
            #this is a modbus register with a single bit [ex: 40003:00]
            startBit = modbusRegister[(colonTokenIndex + 1):]
            bitwiseLength = '1'
    #elif dashTokenIndex >= 0:
    #    #this is a range of registers [ex: 40045-40049]
    #    startRegister = modbusRegister[:dashTokenIndex]
    #    stopBit = modbusRegister[(dashTokenIndex +1 ):]
    #    bitwiseLength = stopBit-startBit+1
    else:
        #This is a modbus register with no bit definition [ex: 40001]
        register = modbusRegister
        startBit = '0'
        bitwiseLength = '16'
    return (register, startBit, bitwiseLength)

def extrapolateRanges(rawData):
    """Takes a list of lists (rows), replaces ranges of CAN objects with rows representing each CAN object,
    returns a list of lists (rows)"""

    #TODO: extrapolate modbus register cell and change ranges to reflect extrapolation
    data = []
    canObjectIndex = findIndex('CAN Object', rawData[0])
    modbusRegisterIndex = findIndex('Modbus Register', rawData[0])
    lengthIndex = findIndex('Length', rawData[0])
    for i in range(0, len(rawData)):
        row = list(rawData[i])
        canObject = row[canObjectIndex]
        dashIndex = canObject.find('-')
        colonIndex = canObject.find(':')
        if dashIndex >= 0: #is range?
            if colonIndex >= 0: #is a range of subindicies?
                index = int(canObject[:colonIndex], 0)
                startSubIndex = int(canObject[(colonIndex+1):(dashIndex)], 0)
                endSubIndex = int(canObject[(dashIndex+1):],0)
                for j in range(startSubIndex, (endSubIndex+1)):
                    newRow = list(row)
                    newRow[canObjectIndex] = hex(index)+':'+hex(j)
                    data.append(newRow)
            else: #is a range of indicies
                startIndex = int(canObject[:dashIndex], 0)
                endIndex = int(canObject[(dashIndex+1):], 0)
                for j in range(startIndex, (endIndex + 1)):
                    newRow = list(row)
                    #
                    data.append(newRow)
        else:
            data.append(row)
    return data

def invertListOfLists(list):
    """Inverts a list of lists, returns a list of lists"""
    list = zip(*list)
    list = [x for x in list]
    return list

def cleanString(string):
    string = string.replace('[1]', '') #remove canopencomm prefix
    string = string.replace(' ','') #remove extra white space
    string = string.replace('\n', '')
    string = string.replace('\r', '')
    string = string.replace(',', '')
    return string

def mapDataType(string):
    if string.lower() == 'uint8':
        return 'u8'
    elif string.lower() == 'uint16':
        return 'u16'
    elif string.lower() == 'uint32':
        return 'u32'
    elif string.lower() == 'int8':
        return 'i8'
    elif string.lower() == 'int16':
        return 'i16'
    elif string.lower() == 'int32':
        return 'i32'
    elif string.lower() == 'visible_string':
        return 'string'
    elif string.lower() == 'bool':
        return 'b'
    else:
        return string

def isNumber(string):
    try:
        assert isinstance(string, int)
        return True
    except:
        pass
    try:
        int(string, 0)
        return True
    except (TypeError, ValueError):
        pass
    try:
        unicodedata.numeric(string)
        return True
    except (TypeError, ValueError):
        pass
    return False

def cellsToValues(sheet):
    """Takes openpyxl.worksheet.read_only.ReadOnlyWorksheet object and returns a list of lists of strings"""
    data = []
    for row in sheet.rows:
        rowValues = []
        for cell in row:
            value = cell.value
            value = str.replace(str(value), '\n', ' ')
            rowValues.append(value)
        data.append(rowValues)
    del data[0:7]
    return data

def removeExtraColumns(data):
    """Remove the columns that have None as header"""
    oldData = invertListOfLists(data) #now we have list of lists (columns)
    newData = []
    for column in oldData:
        if column[0] != 'None':
            newData.append(column)
    newData = invertListOfLists(newData)
    return newData

def extrapolateRanges(rawData):
    """Takes a list of lists (rows), replaces ranges of CAN objects with rows representing each CAN object,
    returns a list of lists (rows)"""
    data = []
    canObjectIndex = findIndex('can_object', rawData[0])
    modbusRegisterIndex = findIndex('modbus_register', rawData[0])
    lengthIndex = findIndex('length', rawData[0])
    for i in range(0, len(rawData)):
        row = list(rawData[i])
        canObject = row[canObjectIndex]
        dashIndex = canObject.find('-')
        colonIndex = canObject.find(':')
        if dashIndex >= 0: #is range?
            if colonIndex >= 0: #is a range of subindicies?
                index = int(canObject[:colonIndex], 0)
                startSubIndex = int(canObject[(colonIndex+1):(dashIndex)], 0)
                endSubIndex = int(canObject[(dashIndex+1):],0)
                for j in range(startSubIndex, (endSubIndex+1)):
                    newRow = list(row)
                    newRow[canObjectIndex] = hex(index)+':'+hex(j)
                    newRow[lengthIndex] = 1
                    data.append(newRow)
            else: #is a range of indicies
                startIndex = int(canObject[:dashIndex], 0)
                endIndex = int(canObject[(dashIndex+1):], 0)
                for j in range(startIndex, (endIndex + 1)):
                    newRow = list(row)
                    # assign new value to CAN object
                    newRow[canObjectIndex] = hex(j)
                    # assign new value to modbus address
                    newRow[modbusRegisterIndex] = j - 8192 + 40001
                    # assign new value to length
                    newRow[lengthIndex] = 1
                    data.append(newRow)
        else:
            data.append(row)
    return data