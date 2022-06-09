import json;
import grpc;
import sys;
sys.path.insert(0,'/home/nadoum/PFE/grpc/');
import configManager_pb2 as configPb2;
import configManager_pb2_grpc as configGrpc;
from concurrent import futures;


class ConfigService(configGrpc.ConfigManagerServicer):
  def readJson(self):
    with open("/home/nadoum/PFE/configManager/config.json",'r') as jsonFile:
      data=json.load(jsonFile);
      return data;


  def getMQTTConfig(self, req, ctx):
    print("[ConfigServer]: Request for MQTT config");
    try:
      data=self.readJson();
      return self.makeMQTTResponse(data);
    except FileNotFoundError:
      print("[ConfigServer]: Json Config file not found");


  def getModbusTCPConfig(self, req, ctx):
    print("[ConfigServer]: Request for ModbusTCP config");
    try:
      data=self.readJson();
      return self.makeModbusTCPResponse(data);
    except FileNotFoundError:
      print("[ConfigServer]: Json Config file not found");


  def makeMQTTResponse(self,jsonData):
    mqttConfig=jsonData["MQTT"];
    brokerConfig=jsonData["Broker"];

    return configPb2.MQTTConfigResponse(
      mqttIp=mqttConfig["MQTTServerIP"]
      ,mqttPort=mqttConfig["MQTTServerPort"]
      ,brokerIp=brokerConfig["BrokerIP"]
      ,brokerPort=brokerConfig["BrokerPort"]
    );


  def makeModbusTCPResponse(self, jsonData):
    modbusTCPConfig=jsonData["ModbusTCP"];
    mqttConfig=jsonData["MQTT"];

    return configPb2.ModbusTCPConfigResponse(
      serverIp=modbusTCPConfig["ModbusTCPServerIP"]
      ,serverPort=modbusTCPConfig["ModbusTCPServerPort"]
      ,mqttIp=mqttConfig["MQTTServerIP"]
      ,mqttPort=mqttConfig["MQTTServerPort"]
    );


def startServer(configManagerService):
  CONFIG_MANAGER_IP="192.168.1.142";
  CONFIG_MANAGER_PORT=4000;
  SOCKET=f"{CONFIG_MANAGER_IP}:{CONFIG_MANAGER_PORT}";
  server=grpc.server(futures.ThreadPoolExecutor(max_workers=10));
  configGrpc.add_ConfigManagerServicer_to_server(configManagerService, server);
  server.add_insecure_port(SOCKET);
  server.start();
  print(f"[ConfigServer]: Server Listening on {SOCKET}");
  server.wait_for_termination();
