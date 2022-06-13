from pymodbus.client.sync import ModbusTcpClient as ModbusClient;
import grpc;
import time;
import sys;
sys.path.append("../../grpc");
import configManager_pb2 as configPb2;
import configManager_pb2_grpc as configGrpc;
import MQTT_pb2 as mqttPb2;
import MQTT_pb2_grpc as mqttGrpc;

CONFIG_SERVER_IP="127.0.0.1";
CONFIG_SERVER_PORT=4000;

def getConfig():
  SOCKET=f"{CONFIG_SERVER_IP}:{CONFIG_SERVER_PORT}";
  channel = grpc.insecure_channel(SOCKET);
  stub = configGrpc.ConfigManagerStub(channel);
  settings = stub.getModbusTCPConfig(configPb2.NoParam());
  print("[ModbusTCPClient]: Received config successfully...");
  return settings;


class ModbusTCPClient():
  def __init__(self, settings):
    self.MODBUS_SERVER_IP=settings.modbusTCPServerConfig.ip;
    self.MODBUS_SERVER_PORT=settings.modbusTCPServerConfig.port;
    self.modbusClient = ModbusClient(self.MODBUS_SERVER_IP, port=self.MODBUS_SERVER_PORT);
    self.unit=0x1;
    self.modbusClient.connect();

  def getData(self, adr, count):
    modbus_data=self.modbusClient.read_holding_registers(adr, count, unit=self.unit);
    mdata=[byte for byte in modbus_data.registers];
    return mdata;

class MQTTClient():
  def __init__(self, settings):
    self.MQTT_SERVER_IP=settings.mqttServerConfig.ip;
    self.MQTT_SERVER_PORT=settings.mqttServerConfig.port;
    self.SOCKET=f"{self.MQTT_SERVER_IP}:{self.MQTT_SERVER_PORT}";

    self.channel = grpc.insecure_channel(self.SOCKET);
    self.stub=mqttGrpc.MQTTServiceStub(self.channel);

  def publish(self, topic, msg):
    print(f"[ModbusTCPClient]: publish(msg={msg}, topic={topic})");
    self.stub.publish(mqttPb2.PublishRequest(topic=topic, msg=msg));
