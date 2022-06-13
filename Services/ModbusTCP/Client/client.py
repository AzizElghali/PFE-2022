import ClientUtils as utils;

# Modbus library
def run():
  settings=utils.getConfig();
  modbusTCPClient=utils.ModbusTCPClient(settings);
  modbusTCPServerData=modbusTCPClient.getData(0,2);
  MQTTClient=utils.MQTTClient(settings);
  print(modbusTCPServerData);
  topic=input("Enter mqtt topic: ");
  list(map(lambda byte :MQTTClient.publish(topic, str(byte)), modbusTCPServerData));


if __name__ == '__main__':
  try:
    run()
  except KeyboardInterrupt:
    print("[ModbusClient]: Shutting down ..")
