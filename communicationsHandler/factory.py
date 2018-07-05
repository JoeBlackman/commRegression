from communicationsHandler.protocol import modbus
from communicationsHandler.protocol import ascobusII
from communicationsHandler.protocol import canopenSDO
from communicationsHandler.transport import serial
from communicationsHandler.transport import ethernet
from communicationsHandler.transport import canbus

class abstractFactory:
    def __init__(self):
        pass
    def getProtocol(self, protocol):
        pass
    def getTransport(self, transport):
        pass

#todo: decide what input argument is (type and where it comes from)
class protocolFactory(abstractFactory):
    def __init__(self):
        abstractFactory.__init__(self)
    def getProtocol(self, protocol):
        if protocol.upper() == 'MODBUS':
            p = modbus()
            return p
        elif protocol.upper() == 'CANOPENSDO':
            p = canopenSDO()
            return p
        #elif protocol.upper() == 'ASCOBUSII':
        #    p = ascobusII()
        #    return p
        else:
            return None

#todo: decide what input argument is (type and where it comes from)
class transportFactory(abstractFactory):
    def __init__(self):
        abstractFactory.__init__(self)
    def getTransport(self, transport):
        if transport.upper() == 'SERIAL':
            t = serial()
            return t
        elif transport.upper() == 'ETHERNET':
            t = ethernet()
            return t
        elif transport.upper() == 'CANBUS':
            t = canbus()
            return t