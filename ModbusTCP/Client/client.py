import ClientUtils as utils;

# Modbus library
def run():
  settings=utils.getConfig();
  modbusTCPClient=utils.ModbusTCPClient(settings);
  modbusTCPServerData=modbusTCPClient.getData(0x0,2);
  MQTTClient=utils.MQTTClient(settings);
  list(map(lambda byte :MQTTClient.publish("/Modbus/Client", str(byte)), modbusTCPServerData));
  


if __name__ == '__main__':
    try:
      run()
    except KeyboardInterrupt:
      print("[ModbusClient]: Shutting down ..")
