"""Modbus TCP server Simulation"""
from pymodbus.server.sync import StartTcpServer
from pymodbus.device import ModbusDeviceIdentification
from pymodbus.datastore import ModbusSequentialDataBlock
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext

# Server data
DATABLOCK = [i for i in range(10)]

def run_server():
    """initialize the server information"""
    store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0, DATABLOCK), zero_mode=True)
    context = ModbusServerContext(slaves=store, single=True)
    identity = ModbusDeviceIdentification()
    identity.VendorName = 'DATAKOM WATER METER/VALVE SIMULATOR'
    identity.ProductCode = 'DATAKOM DKM-407'
    identity.VendorUrl = 'https://sofia-technologies.com/'
    identity.ProductName = 'Water meter/valve'
    identity.ModelName = 'Water valve/meter DATAKOM DKM-407'
    identity.MajorMinorRevision = '1.1'

    print("[ModbusTCP] Starting Server ..")
    StartTcpServer(context, identity=identity, address=("127.0.0.1", 5001))

if __name__ == "__main__":
    run_server()
