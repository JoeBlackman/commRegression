class connection():
    def __init__(self, id = None, can_node_id=None, can_baud_rate=None, ip_address=None, tcp_port=None, tcp_unit_id=None,
                 serial_port=None, serial_unit_id=None, serial_baud_rate=None, serial_byte_size=None,
                 serial_parity=None, serial_stop_bits=None, serial_xonxoff=None, serial_timeout=None, protocol=None,
                 transport=None):
        self.id = id
        self.can_node_id = can_node_id
        self.can_baud_rate = can_baud_rate
        self.ip_address = ip_address
        self.tcp_port = tcp_port
        self.tcp_unit_id = tcp_unit_id
        self.serial_port = serial_port
        self.serial_unit_id = serial_unit_id
        self.serial_baud_rate = serial_baud_rate
        self.serial_byte_size = serial_byte_size
        self.serial_parity = serial_parity
        self.serial_stop_bits = serial_stop_bits
        self.serial_xonxoff = serial_xonxoff
        self.serial_timeout = serial_timeout
        self.protocol = protocol
        self.transport = transport