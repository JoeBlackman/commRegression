
from communicationsHandler.factory import protocolFactory
from communicationsHandler.factory import transportFactory

def readProtocolData(connectionid, communicationObjectId):

    protocol = 'canopensdo' #from connection
    transport = 'canbus' #from connection
    ipAddress = '169.254.1.1' #from connection
    tcpPort = 502 #from connection
    unitIdTcp = 1 #from connection
    serialPort = 'COM1' #from connection
    serialBaudRate = 9600 #from connection
    serialByteSize = 8 #from connection
    serialParity = 'N' #from connection
    serialStopBits = 1 #from connection
    serialXonXoff = 0 #from connection
    unitIdSerial = 1 #from connection
    modbusRegister = 13 #from communicationObjectId
    length = 1 #from communicationObjectId
    canNodeId = '0x10'
    canIndex = '0x2000' #from communicationObjectId
    canSubIndex = '0x00' #from communicationObjectId
    dataType = 'u16' #from communicationObjectId
    writeValue = '0x0000' #contrived
    tfact = transportFactory()
    t = tfact.getTransport(transport)  # from connection
    t.ipaddress = ipAddress  # from connection
    t.tcpPort = tcpPort  # from connection
    t.serialport = serialPort
    t.serialbaudrate = serialBaudRate
    t.serialbytesize = serialByteSize
    t.serialparity = serialParity
    t.serialstopbits = serialStopBits
    t.serialxonxoff = serialXonXoff
    t.cannodeid = canNodeId
    pfact = protocolFactory()
    p = pfact.getProtocol(protocol)  # from connection
    p.transport = t  # from this method
    p.modbusregister = modbusRegister  # from commmunication object
    p.length = length  # from communication object
    p.unitidtcp = unitIdTcp  # from connection
    p.modbusregister = modbusRegister
    p.length = length
    p.unitidserial = unitIdSerial
    p.canindex = canIndex
    p.cansubindex = canSubIndex
    p.datatype = dataType
    p.writeValue = writeValue
    return p.read()

def writeProtocolData():
    pass