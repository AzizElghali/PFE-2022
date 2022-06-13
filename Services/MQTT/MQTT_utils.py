import paho.mqtt.client as paho;
import time;
import grpc;
import sys;
from concurrent import futures;
sys.path.append("../grpc");
import MQTT_pb2 as mqttPb2;
import MQTT_pb2_grpc as mqttGrpc;
import configManager_pb2 as configPb2;
import configManager_pb2_grpc as configGrpc;

CONFIG_SERVER_IP = "localhost";
CONFIG_SERVER_PORT = 4000;

def getConfig():
  SOCKET=f"{CONFIG_SERVER_IP}:{CONFIG_SERVER_PORT}";
  channel = grpc.insecure_channel(SOCKET);
  stub = configGrpc.ConfigManagerStub(channel);
  settings = stub.getMQTTConfig(configPb2.NoParam());
  print("[MQTTServer]: Received config successfully...");
  return settings;

def on_publish(client,userdata,result):
  print(f"[MQTTServer]: (Publish) {result}");

class MQTTService(mqttGrpc.MQTTServiceServicer):
  def __init__(self, settings):
    self.ip=settings.mqttServerConfig.ip;
    self.port=settings.mqttServerConfig.port;
    self.brokerIp=settings.brokerConfig.ip;
    self.brokerPort=settings.brokerConfig.port;
    self.socket=f"{self.ip}:{self.port}";
    self.mqttc=paho.Client(client_id="**[MQTTServer]**");
    self.mqttc.on_publish=on_publish;

  def publish(self, req, ctx):
    self.connectToBroker();
    self.mqttc.publish(req.topic, req.msg);
    self.disconnectFromBroker();
    return mqttPb2.NoParam();

  def connectToBroker(self):
    self.mqttc.connect(self.brokerIp, self.brokerPort, 60);

  def disconnectFromBroker(self):
    self.mqttc.disconnect();


def startServer(mqttService):
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10));
  mqttGrpc.add_MQTTServiceServicer_to_server(mqttService, server);
  server.add_insecure_port(mqttService.socket);
  server.start();
  print(f"[MQTTServer]: Server Listening on Socket: {mqttService.socket}");
  server.wait_for_termination();
