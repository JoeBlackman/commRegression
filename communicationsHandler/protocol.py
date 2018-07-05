#import drivers here?
import utilities
import RDCanOpenWrapper
import serial
import modbus_tk.defines as cst
from modbus_tk import modbus_tcp, modbus_rtu

class protocol:
    def __init__(self, transport):
        self.unitidtcp = None
        self.unitidserial = None
        self.transport = transport
        self.modbusregister = None
        self.startbit = None
        self.bitwiselength = None
        self.canindex = None
        self.cansubindex = None
        self.datatype = None
        self.length = None
        self.writeValue = None
    def read(self):
        pass
    def write(self):
        pass

class modbus(protocol):
    def __init__(self, transport = None):
        protocol.__init__(self, transport)
    def read(self):
        if repr(self.transport) == 'transport.ethernet':
            tcpMaster = modbus_tcp.TcpMaster(self.transport.ipAddress, self.transport.tcpPort)
            readValue = tcpMaster.execute(slave=self.unitidtcp, function_code=cst.READ_HOLDING_REGISTERS,
                                               starting_address=self.modbusregister, quantity_of_x=self.length)
            tcpMaster.close()
            return readValue
        elif repr(self.transport) == 'transport.serial':
            rtuMaster = modbus_rtu.RtuMaster(serial.Serial(
                port=self.transport.serialport, baudrate=self.transport.serialbaudrate,
                bytesize=self.transport.serialbytesize, parity=self.transport.serialparity,
                stopbits=self.transport.serialstopbits, xonxoff=self.transport.serialxonxoff))
            rtuMaster.set_timeout(self.transport.serialtimeout)
            readValue = rtuMaster.execute(slave=self.unitidserial, function_code=cst.READ_HOLDING_REGISTERS,
                                                  starting_address=self.modbusregister, quantity_of_x=self.length)
            rtuMaster.close()
            return readValue
        else:
            pass
    def write(self):
        if repr(self.transport) == 'transport.ethernet':
            tcpMaster = modbus_tcp.TcpMaster(self.transport.ipAddress, self.transport.tcpPort)
            writeStatus = tcpMaster.execute(slave=self.unitidtcp, function_code=cst.WRITE_MULTIPLE_REGISTERS,
                                            starting_address=self.modbusregister, quantity_of_x=self.length,
                                            output_value= self.writeValue)
            tcpMaster.close()
            return writeStatus
        elif repr(self.transport) == 'transport.serial':
            rtuMaster = modbus_rtu.RtuMaster(serial.Serial(
                port=self.transport.serialport, baudrate=self.transport.serialbaudrate,
                bytesize=self.transport.serialbytesize, parity=self.transport.serialparity,
                stopbits=self.transport.serialstopbits, xonxoff=self.transport.serialxonxoff,
                timeout=self.transport.serialtimeout))
            writeStatus = rtuMaster.execute(slave=self.unitidserial, function_code=cst.READ_HOLDING_REGISTERS,
                                           starting_address=self.modbusregister, quantity_of_x=self.length,
                                           output_value=self.writeValue)
            rtuMaster.close()
            return writeStatus

class ascobusII(protocol):
    def __init__(self, transport = None):
        protocol.__init__(self, transport)
    def read(self):
        if repr(self.transport) == 'transport.ethernet':
            pass
        elif repr(self.transport) == 'transport.serial':
            pass
        else:
            pass
    def write(self):
        pass

class canopenSDO(protocol):
    def __init__(self, transport = None):
        protocol.__init__(self, transport)
    def read(self):
        if repr(self.transport) == 'transport.canbus':
            readValue = RDCanOpenWrapper.callcanopencomm(self.transport.cannodeid,
                                                         'r',
                                                         self.canindex,
                                                         self.cansubindex,
                                                         self.datatype)
            readValue = [utilities.cleanString(x.decode('utf-8')) for x in readValue]
            return readValue
        else:
            pass
    def write(self):
        if repr(self.transport) == 'transport.canbus':
            writeStatus = RDCanOpenWrapper.callcanopencomm(self.transport.nodeid,
                                                           'w',
                                                           self.canindex,
                                                           self.cansubindex,
                                                           self.datatype,
                                                           self.writeValue)
            writeStatus = [utilities.cleanString(x.decode('utf-8')) for x in writeStatus]
            return writeStatus
        else:
            pass
