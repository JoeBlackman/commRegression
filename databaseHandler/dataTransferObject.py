'''Data Transfer Object for a communication object'''
class dataTransferObject:
    def __init__(self):
        pass

class testDTO(dataTransferObject):
    def __init__(self, id = None, can_object = None, modbus_register = None, user = None, canbus_canopensdo_access = None,
                 canbus_canopenpdo_access = None, ethernet_ascobus2_access = None, ethernet_modbus_access = None,
                 rs485_ascobus2_access = None, rs485_modbus_access = None, ttl_ascobus2_access = None,
                 ttl_modbus_access = None, parameter_name = None, parameter_description = None, data_type = None,
                 length = None, data_range_min = None, data_range_max = None, data_range_multiplier = None,
                 supported_firmware_version = None, unit = None, note = None, test_type = None, connection_id = None,
                 read_value = None, write_value = None, expected_value = None, error_message = None, test_result = None):
        dataTransferObject.__init__(self)
        self.id = id
        self.can_object = can_object
        self.modbus_register = modbus_register
        self.user = user
        self.canbus_canopensdo_access = canbus_canopensdo_access
        self.canbus_canopenpdo_access = canbus_canopenpdo_access
        self.ethernet_ascobus2_access = ethernet_ascobus2_access
        self.ethernet_modbus_access = ethernet_modbus_access
        self.rs485_ascobus2_access = rs485_ascobus2_access
        self.rs485_modbus_access = rs485_modbus_access
        self.ttl_ascobus2_access = ttl_ascobus2_access
        self.ttl_modbus_access = ttl_modbus_access
        self.parameter_name = parameter_name
        self.parameter_description = parameter_description
        self.data_type = data_type
        self.length = length
        self.data_range_min = data_range_min
        self.data_range_max = data_range_max
        self.data_range_multiplier = data_range_multiplier
        self.supported_firmware_version = supported_firmware_version
        self.unit = unit
        self.note = note
        self.test_type = test_type
        self.connection_id = connection_id
        self.read_value = read_value
        self.write_value = write_value
        self.expected_value = expected_value
        self.error_message = error_message
        self.test_result = test_result

class connectionDTO(dataTransferObject):
    def __init__(self, id = None, can_node_id=None, can_baud_rate=None, ip_address=None, tcp_port=None, tcp_unit_id=None,
                 serial_port=None, serial_unit_id=None, serial_baud_rate=None, serial_byte_size=None,
                 serial_parity=None, serial_stop_bits=None, serial_xonxoff=None, serial_timeout=None, protocol=None):
        dataTransferObject.__init__(self)
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