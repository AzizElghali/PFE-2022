import ConfigManagerUtils as utils;

def serve():
  configManagerService = utils.ConfigService();
  utils.startServer(configManagerService);


if __name__ == "__main__":
  try:
    serve();
  except KeyboardInterrupt:
    print("[ConfigServer]: shutting down...");
