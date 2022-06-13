from operator import itemgetter
import json;
import grpc;
import sys;
sys.path.append('../grpc/');
import configManager_pb2 as configPb2;
import configManager_pb2_grpc as configGrpc;
from concurrent import futures;

CONFIG_MANAGER_IP="127.0.0.1";
CONFIG_MANAGER_PORT=4000;


class ConfigService(configGrpc.ConfigManagerServicer):
  def readJson(self):
    with open("config.json",'r') as jsonFile:
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
    mqttConfigJson=jsonData["MQTT"];
    brokerConfigJson=jsonData["Broker"];

    return configPb2.MQTTConfigResponse(
      mqttServerConfig=configPb2.Socket(
        ip=mqttConfigJson["ip"]
        ,port=mqttConfigJson["port"]
      )
      ,brokerConfig=configPb2.Socket(
        ip=brokerConfigJson["ip"]
        ,port=brokerConfigJson["port"]
      )
    );


  def makeModbusTCPResponse(self, jsonData):
    modbusTCPConfigJson=jsonData["ModbusTCPServer"];
    mqttConfigJson=jsonData["MQTT"];
    return configPb2.ModbusTCPConfigResponse(
      modbusTCPServerConfig=configPb2.Socket(
        ip=modbusTCPConfigJson["ip"]
       ,port=modbusTCPConfigJson["port"]),
      mqttServerConfig=configPb2.Socket(
        ip=mqttConfigJson["ip"]
        ,port=mqttConfigJson["port"]
      )
    );


def startServer(configManagerService):
  SOCKET=f"{CONFIG_MANAGER_IP}:{CONFIG_MANAGER_PORT}";
  server=grpc.server(futures.ThreadPoolExecutor(max_workers=10));
  configGrpc.add_ConfigManagerServicer_to_server(configManagerService, server);
  server.add_insecure_port(SOCKET);
  server.start();
  print(f"[ConfigServer]: Server Listening on {SOCKET}");
  server.wait_for_termination();
