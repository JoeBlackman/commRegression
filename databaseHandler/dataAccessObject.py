'''Data Access Object for a communication object'''
from sqlalchemy import create_engine
from sqlalchemy import Table
from sqlalchemy import MetaData
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import select

class dataAccessObject:
    def __init__(self):
        self.databasePath = None
        self.table = None

    #DROP table
    def drop(self):
        engine = create_engine(self.databasePath, echo=True)
        metadata = MetaData()
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        table.drop(engine, checkfirst=True)

    #SELECT row from table
    def select(self, id):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = table.select().where(table.c.id == id)
        results = connection.execute(stmt).fetchone()
        #TODO: should this return a data transfer object?
        return results

    #select all table entries
    def selectAll(self):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = select([table])
        results = connection.execute(stmt).fetchall()
        return results

class testDAO(dataAccessObject):
    def __init__(self):
        dataAccessObject.__init__(self)
        self.databasePath = 'sqlite:///regression.db'
        self.table = 'tests'

    #CREATE table
    def create(self):
        engine = create_engine(self.databasePath, echo=True)
        metadata = MetaData()
        table = Table(self.table, metadata,
                    Column('id', Integer, primary_key=True),
                    Column('can_object', String),
                    Column('modbus_register', String),
                    Column('user', String),
                    Column('canbus_canopensdo_access', String),
                    Column('canbus_canopenpdo_access', String),
                    Column('ethernet_ascobus2_access', String),
                    Column('ethernet_modbus_access', String),
                    Column('rs485_ascobus2_access', String),
                    Column('rs485_modbus_access', String),
                    Column('ttl_ascobus2_access', String),
                    Column('ttl_modbus_access', String),
                    Column('parameter_name', String),
                    Column('parameter_description', String),
                    Column('data_type', String),
                    Column('length', String),
                    Column('data_range_min', String),
                    Column('data_range_max', String),
                    Column('data_range_multiplier', String),
                    Column('supported_firmware_version', String),
                    Column('unit', String),
                    Column('note', String),
                    Column('test_type', String),
                    Column('connection_id', String),
                    Column('read_value', String),
                    Column('write_value', String),
                    Column('expected_value', String),
                    Column('error_message', String),
                    Column('test_result', String))
        table.create(engine, checkfirst=True)

    #INSERT INTO table
    def insert(self, dto):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = table.insert().values(can_object=dto.can_object,
                                     modbus_register=dto.modbus_register,
                                     user=dto.user,
                                     canbus_canopensdo_access=dto.canbus_canopensdo_access,
                                     canbus_canopenpdo_access=dto.canbus_canopenpdo_access,
                                     ethernet_ascobus2_access=dto.ethernet_ascobus2_access,
                                     ethernet_modbus_access=dto.ethernet_modbus_access,
                                     rs485_ascobus2_access=dto.rs485_ascobus2_access,
                                     rs485_modbus_access=dto.rs485_modbus_access,
                                     ttl_ascobus2_access=dto.ttl_ascobus2_access,
                                     ttl_modbus_access=dto.ttl_modbus_access,
                                     parameter_name=dto.parameter_name,
                                     parameter_description=dto.parameter_description,
                                     data_type=dto.data_type,
                                     length=dto.length,
                                     data_range_min=dto.data_range_min,
                                     data_range_max=dto.data_range_max,
                                     data_range_multiplier=dto.data_range_multiplier,
                                     supported_firmware_version=dto.supported_firmware_version,
                                     unit=dto.unit,
                                     note=dto.note,
                                     test_type=dto.test_type,
                                     connection_id=dto.connection_id,
                                     read_value=dto.read_value,
                                     write_value=dto.write_value,
                                     expected_value=dto.expected_value,
                                     error_message=dto.error_message,
                                     test_result=dto.test_result)
        result = connection.execute(stmt)

    #UPDATE - the toughest to write
    def update(self, dto):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = table.update().where(table.c.id == dto.id).values(can_object=dto.can_object,
                                                         modbus_register=dto.modbus_register,
                                                         user=dto.user,
                                                         canbus_canopensdo_access=dto.canbus_canopensdo_access,
                                                         canbus_canopenpdo_access=dto.canbus_canopenpdo_access,
                                                         ethernet_ascobus2_access=dto.ethernet_ascobus2_access,
                                                         ethernet_modbus_access=dto.ethernet_modbus_access,
                                                         rs485_ascobus2_access=dto.rs485_ascobus2_access,
                                                         rs485_modbus_access=dto.rs485_modbus_access,
                                                         ttl_ascobus2_access=dto.ttl_ascobus2_access,
                                                         ttl_modbus_access=dto.ttl_modbus_access,
                                                         parameter_name=dto.parameter_name,
                                                         parameter_description=dto.parameter_description,
                                                         data_type=dto.data_type,
                                                         length=dto.length,
                                                         data_range_min=dto.data_range_min,
                                                         data_range_max=dto.data_range_max,
                                                         data_range_multiplier=dto.data_range_multiplier,
                                                         supported_firmware_version=dto.supported_firmware_version,
                                                         unit=dto.unit,
                                                         note=dto.note,
                                                         test_type=dto.test_type,
                                                         connection_id=dto.connection_id,
                                                         read_value=dto.read_value,
                                                         write_value=dto.write_value,
                                                         expected_value=dto.expected_value,
                                                         error_message=dto.expected_value,
                                                         test_result=dto.test_result)
        result = connection.execute(stmt)

class connectionDAO(dataAccessObject):
    def __init__(self):
        dataAccessObject.__init__(self)
        self.databasePath = 'sqlite:///regression.db'
        self.table = 'connections'

    # CREATE table
    def create(self):
        engine = create_engine(self.databasePath, echo=True)
        metadata = MetaData()
        table = Table(self.table, metadata,
                      Column('id', Integer, primary_key=True),
                      Column('can_node_id', String),
                      Column('can_baud_rate', String),
                      Column('ip_address', String),
                      Column('tcp_port', String),
                      Column('tcp_unit_id', String),
                      Column('serial_port', String),
                      Column('serial_unit_id', String),
                      Column('serial_baud_rate', String),
                      Column('serial_byte_size', String),
                      Column('serial_parity', String),
                      Column('serial_stop_bits', String),
                      Column('serial_xonxoff', String),
                      Column('serial_timeout', String),
                      Column('protocol', String))
        table.create(engine, checkfirst=True)

    # INSERT INTO table
    def insert(self, dto):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = table.insert().values(can_node_id=dto.can_node_id,
                                     can_baud_rate=dto.can_baud_rate,
                                     ip_address=dto.ip_address,
                                     tcp_port=dto.tcp_port,
                                     tcp_unit_id=dto.tcp_unit_id,
                                     serial_port=dto.serial_port,
                                     serial_unit_id=dto.serial_unit_id,
                                     serial_baud_rate=dto.serial_baud_rate,
                                     serial_byte_size=dto.serial_byte_size,
                                     serial_parity=dto.serial_parity,
                                     serial_stop_bits=dto.serial_stop_bits,
                                     serial_xonxoff=dto.serial_xonxoff,
                                     serial_timeout=dto.serial_timeout,
                                     protocol=dto.protocol)
        result = connection.execute(stmt)

    #UPDATE - update a row of the table with new information (need id of row to update, and row info)
    def update(self, dto):
        engine = create_engine(self.databasePath, echo=True)
        connection = engine.connect()
        metadata = MetaData(engine)
        table = Table(self.table, metadata, autoload=True, autoload_with=engine)
        stmt = table.update().where(table.c.id==dto.id).values(can_node_id=dto.can_node_id,
                                                               can_baud_rate=dto.can_node_id,
                                                               ip_address=dto.ip_address,
                                                               tcp_port=dto.tcp_port,
                                                               tcp_unit_id=dto.tcp_unit_id,
                                                               serial_port=dto.serial_port,
                                                               serial_unit_id=dto.serial_unit_id,
                                                               serial_baud_rate=dto.serial_baud_rate,
                                                               serial_byte_size=dto.serial_byte_size,
                                                               serial_parity=dto.serial_parity,
                                                               serial_stop_bits=dto.serial_stop_bits,
                                                               serial_xonxoff=dto.serial_xonxoff,
                                                               serial_timeout=dto.serial_timeout,
                                                               protocol=dto.protocol)
        result = connection.execute(stmt)