import MQTT_utils as utils;

def serve():
  settings = utils.getConfig();
  mqttServiceWithSettings=utils.MQTTService(settings);
  utils.startServer(mqttServiceWithSettings);


if __name__ == "__main__":
  try:
    serve();
  except KeyboardInterrupt:
    print("[MQTTServer]: Shutting down...");
