# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: get_config.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x10get_config.proto\x12\nget_config\";\n\x07Request\x12\x0c\n\x04host\x18\x01 \x01(\t\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x10\n\x08password\x18\x03 \x01(\t\"\x18\n\x05Reply\x12\x0f\n\x07message\x18\x01 \x01(\t2D\n\nget_config\x12\x36\n\nLogin_info\x12\x13.get_config.Request\x1a\x11.get_config.Reply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'get_config_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REQUEST']._serialized_start=32
  _globals['_REQUEST']._serialized_end=91
  _globals['_REPLY']._serialized_start=93
  _globals['_REPLY']._serialized_end=117
  _globals['_GET_CONFIG']._serialized_start=119
  _globals['_GET_CONFIG']._serialized_end=187
# @@protoc_insertion_point(module_scope)
