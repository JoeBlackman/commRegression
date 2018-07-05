class transport:
    def __init__(self):
        self.ipaddress = None
        self.tcpport = None
        self.serialport = None
        self.serialbaudrate = None
        self.serialbytesize = None
        self.serialparity = None
        self.serialstopbits = None
        self.serialxonxoff = None
        self.serialtimeout = None
        self.cannodeid = None
        self.canbaudrate = None
        self.isConnected = False

class ethernet(transport):
    def __init__(self):
        transport.__init__(self)
    def __repr__(self):
        return 'transport.ethernet'

class serial(transport):
    def __init__(self):
        transport.__init__(self)
    def __repr__(self):
        return 'transport.serial'

class canbus(transport):
    def __init__(self):
        transport.__init__(self)
    def __repr__(self):
        return 'transport.canbus'