'''test object'''
class test():
    def __init__(self, id = None, can_object = None, modbus_register = None, user = None, canbus_canopensdo_access = None,
                 canbus_canopenpdo_access = None, ethernet_ascobus2_access = None, ethernet_modbus_access = None,
                 rs485_ascobus2_access = None, rs485_modbus_access = None, ttl_ascobus2_access = None,
                 ttl_modbus_access = None, parameter_name = None, parameter_description = None, data_type = None,
                 length = None, data_range_min = None, data_range_max = None, data_range_multiplier = None,
                 supported_firmware_version = None, unit = None, note = None, test_type = None, connection_id = None,
                 read_value = None, write_value = None, expected_value = None, error_message = None, test_result = None):
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

    def setup(self):
        #extra variable assignments and connections checking go here
        pass

    def run(self):
        pass
        #validation business logic goes here
        #reads and writes invoked by calling communicationsWrapper.readProtocolData or
        # communicationsWrapper.writeProtocolData

    def teardown(self):
        #tear down connections here
        pass

class singleReadTest(test):
    def __init__(self):
        test.__init__(self)

    def setup(self):
        pass

    def run(self):
        pass

    def teardown(self):
        pass

class writeScanTest(test):
    def __init__(self):
        test.__init__(self)
        self.failureThreshold = 10
        self.failures = []

    def setup(self):
        pass

    def run(self):
        pass

    def teardown(self):
        pass

class boundaryCheckTest(test):
    def __init__(self):
        test.__init__(self)
        self.failureThreshold = 10
        self.failures = []

    def setup(self):
        pass

    def run(self):
        pass

    def teardown(self):
        pass

class writeToReadOnlyTest(test):
    def __init__(self):
        test.__init__(self)

    def setup(self):
        pass

    def run(self):
        pass

    def teardown(self):
        pass