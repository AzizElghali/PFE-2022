"""Modbus TCP server Simulation"""
from pymodbus.server.sync import StartTcpServer;
from pymodbus.device import ModbusDeviceIdentification;
from pymodbus.datastore import ModbusSequentialDataBlock;
from pymodbus.datastore import ModbusSlaveContext, ModbusServerContext;

DATABLOCK = [i for i in range(10)];
IP="127.0.0.1";
PORT=5001;
SOCKET=f"{IP}:{PORT}";

def run_server():
  store = ModbusSlaveContext(hr=ModbusSequentialDataBlock(0, DATABLOCK), zero_mode=True);
  context = ModbusServerContext(slaves=store, single=True);
  identity = ModbusDeviceIdentification();
  identity.VendorName = 'DATAKOM WATER METER/VALVE SIMULATOR';
  identity.ProductCode = 'DATAKOM DKM-407';
  identity.VendorUrl = 'https://sofia-technologies.com/';
  identity.ProductName = 'Water meter/valve';
  identity.ModelName = 'Water valve/meter DATAKOM DKM-407';
  identity.MajorMinorRevision = '1.1';
  print(f"[ModbusTCP]: Starting Server at {SOCKET}");
  StartTcpServer(context, identity=identity, address=(IP, PORT));

if __name__ == "__main__":
    run_server();
