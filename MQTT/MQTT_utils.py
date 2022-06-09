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


def getConfig():
  configServerIp = "192.168.1.142";
  configServerPort = 4000;
  channel = grpc.insecure_channel(f"{configServerIp}:{configServerPort}");
  stub = configGrpc.ConfigManagerStub(channel);
  settings = stub.getMQTTConfig(configPb2.NoParam());
  print("[MQTTServer]: Received config successfully...");
  return settings;

def on_publish(client,userdata,result):
  print(f"[MQTTServer]: (Publish) {result} {userdata}");

class MQTTService(mqttGrpc.MQTTServiceServicer):
  def __init__(self, settings):
    self.ip=settings.mqttIp;
    self.port=settings.mqttPort;
    self.brokerIp = settings.brokerIp;
    self.brokerPort = settings.brokerPort;
    self.socket= f"{self.ip}:{self.port}";
    self.mqttc = paho.Client(client_id="**[MQTTServer]**");
    self.mqttc.on_publish = on_publish;

  def publish(self, req, ctx):
    self.connectToBroker();
    self.mqttc.publish(req.topic, req.message);
    self.disconnectFromBroker();
    return mqttPb2.NoResponse();

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
