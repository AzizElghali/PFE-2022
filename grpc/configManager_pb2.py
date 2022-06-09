# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: configManager.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x63onfigManager.proto\x12\rConfigManager\"\t\n\x07NoParam\"a\n\x17ModbusTCPConfigResponse\x12\x10\n\x08serverIp\x18\x01 \x01(\t\x12\x12\n\nserverPort\x18\x02 \x01(\r\x12\x0e\n\x06mqttIp\x18\x03 \x01(\t\x12\x10\n\x08mqttPort\x18\x04 \x01(\r\"\\\n\x12MQTTConfigResponse\x12\x0e\n\x06mqttIp\x18\x01 \x01(\t\x12\x10\n\x08mqttPort\x18\x02 \x01(\r\x12\x10\n\x08\x62rokerIp\x18\x03 \x01(\t\x12\x12\n\nbrokerPort\x18\x04 \x01(\r2\xb1\x01\n\rConfigManager\x12J\n\rgetMQTTConfig\x12\x16.ConfigManager.NoParam\x1a!.ConfigManager.MQTTConfigResponse\x12T\n\x12getModbusTCPConfig\x12\x16.ConfigManager.NoParam\x1a&.ConfigManager.ModbusTCPConfigResponseb\x06proto3')



_NOPARAM = DESCRIPTOR.message_types_by_name['NoParam']
_MODBUSTCPCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['ModbusTCPConfigResponse']
_MQTTCONFIGRESPONSE = DESCRIPTOR.message_types_by_name['MQTTConfigResponse']
NoParam = _reflection.GeneratedProtocolMessageType('NoParam', (_message.Message,), {
  'DESCRIPTOR' : _NOPARAM,
  '__module__' : 'configManager_pb2'
  # @@protoc_insertion_point(class_scope:ConfigManager.NoParam)
  })
_sym_db.RegisterMessage(NoParam)

ModbusTCPConfigResponse = _reflection.GeneratedProtocolMessageType('ModbusTCPConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _MODBUSTCPCONFIGRESPONSE,
  '__module__' : 'configManager_pb2'
  # @@protoc_insertion_point(class_scope:ConfigManager.ModbusTCPConfigResponse)
  })
_sym_db.RegisterMessage(ModbusTCPConfigResponse)

MQTTConfigResponse = _reflection.GeneratedProtocolMessageType('MQTTConfigResponse', (_message.Message,), {
  'DESCRIPTOR' : _MQTTCONFIGRESPONSE,
  '__module__' : 'configManager_pb2'
  # @@protoc_insertion_point(class_scope:ConfigManager.MQTTConfigResponse)
  })
_sym_db.RegisterMessage(MQTTConfigResponse)

_CONFIGMANAGER = DESCRIPTOR.services_by_name['ConfigManager']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOPARAM._serialized_start=38
  _NOPARAM._serialized_end=47
  _MODBUSTCPCONFIGRESPONSE._serialized_start=49
  _MODBUSTCPCONFIGRESPONSE._serialized_end=146
  _MQTTCONFIGRESPONSE._serialized_start=148
  _MQTTCONFIGRESPONSE._serialized_end=240
  _CONFIGMANAGER._serialized_start=243
  _CONFIGMANAGER._serialized_end=420
# @@protoc_insertion_point(module_scope)