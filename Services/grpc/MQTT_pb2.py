# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: MQTT.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nMQTT.proto\x12\x04MQTT\"\t\n\x07NoParam\",\n\x0ePublishRequest\x12\r\n\x05topic\x18\x01 \x01(\t\x12\x0b\n\x03msg\x18\x02 \x01(\t2=\n\x0bMQTTService\x12.\n\x07publish\x12\x14.MQTT.PublishRequest\x1a\r.MQTT.NoParamb\x06proto3')



_NOPARAM = DESCRIPTOR.message_types_by_name['NoParam']
_PUBLISHREQUEST = DESCRIPTOR.message_types_by_name['PublishRequest']
NoParam = _reflection.GeneratedProtocolMessageType('NoParam', (_message.Message,), {
  'DESCRIPTOR' : _NOPARAM,
  '__module__' : 'MQTT_pb2'
  # @@protoc_insertion_point(class_scope:MQTT.NoParam)
  })
_sym_db.RegisterMessage(NoParam)

PublishRequest = _reflection.GeneratedProtocolMessageType('PublishRequest', (_message.Message,), {
  'DESCRIPTOR' : _PUBLISHREQUEST,
  '__module__' : 'MQTT_pb2'
  # @@protoc_insertion_point(class_scope:MQTT.PublishRequest)
  })
_sym_db.RegisterMessage(PublishRequest)

_MQTTSERVICE = DESCRIPTOR.services_by_name['MQTTService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _NOPARAM._serialized_start=20
  _NOPARAM._serialized_end=29
  _PUBLISHREQUEST._serialized_start=31
  _PUBLISHREQUEST._serialized_end=75
  _MQTTSERVICE._serialized_start=77
  _MQTTSERVICE._serialized_end=138
# @@protoc_insertion_point(module_scope)
