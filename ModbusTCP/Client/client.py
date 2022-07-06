import ClientUtils as utils;
import time

MODBUS_TOPIC = "modbustcp"

# Modbus library
def run():
  settings=utils.getConfig();
  print(f"IP: {settings.modbusTCPServerConfig.ip}, PORT: {settings.modbusTCPServerConfig.port}")
  modbusTCPClient=utils.ModbusTCPClient(settings);
  modbusTCPServerData=modbusTCPClient.getData(0,2);
  MQTTClient=utils.MQTTClient(settings);
  #print(modbusTCPServerData);
  #topic=input("Enter mqtt topic: ");
  list(map(lambda byte :MQTTClient.publish(MODBUS_TOPIC, str(byte)), modbusTCPServerData));


if __name__ == '__main__':
  try:
    while True:
        run()
        time.sleep(2)
  except KeyboardInterrupt:
    print("[ModbusClient]: Shutting down ..")
