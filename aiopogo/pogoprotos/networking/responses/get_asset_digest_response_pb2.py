# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: pogoprotos/networking/responses/get_asset_digest_response.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from pogoprotos.data import asset_digest_entry_pb2 as pogoprotos_dot_data_dot_asset__digest__entry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='pogoprotos/networking/responses/get_asset_digest_response.proto',
  package='pogoprotos.networking.responses',
  syntax='proto3',
  serialized_pb=_b('\n?pogoprotos/networking/responses/get_asset_digest_response.proto\x12\x1fpogoprotos.networking.responses\x1a(pogoprotos/data/asset_digest_entry.proto\"\xfd\x01\n\x16GetAssetDigestResponse\x12\x31\n\x06\x64igest\x18\x01 \x03(\x0b\x32!.pogoprotos.data.AssetDigestEntry\x12\x14\n\x0ctimestamp_ms\x18\x02 \x01(\x04\x12N\n\x06result\x18\x03 \x01(\x0e\x32>.pogoprotos.networking.responses.GetAssetDigestResponse.Result\x12\x13\n\x0bpage_offset\x18\x04 \x01(\x05\"5\n\x06Result\x12\t\n\x05UNSET\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x08\n\x04PAGE\x10\x02\x12\t\n\x05RETRY\x10\x03\x62\x06proto3')
  ,
  dependencies=[pogoprotos_dot_data_dot_asset__digest__entry__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)



_GETASSETDIGESTRESPONSE_RESULT = _descriptor.EnumDescriptor(
  name='Result',
  full_name='pogoprotos.networking.responses.GetAssetDigestResponse.Result',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PAGE', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RETRY', index=3, number=3,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=343,
  serialized_end=396,
)
_sym_db.RegisterEnumDescriptor(_GETASSETDIGESTRESPONSE_RESULT)


_GETASSETDIGESTRESPONSE = _descriptor.Descriptor(
  name='GetAssetDigestResponse',
  full_name='pogoprotos.networking.responses.GetAssetDigestResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='digest', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.digest', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='timestamp_ms', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='result', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.result', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='page_offset', full_name='pogoprotos.networking.responses.GetAssetDigestResponse.page_offset', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _GETASSETDIGESTRESPONSE_RESULT,
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=143,
  serialized_end=396,
)

_GETASSETDIGESTRESPONSE.fields_by_name['digest'].message_type = pogoprotos_dot_data_dot_asset__digest__entry__pb2._ASSETDIGESTENTRY
_GETASSETDIGESTRESPONSE.fields_by_name['result'].enum_type = _GETASSETDIGESTRESPONSE_RESULT
_GETASSETDIGESTRESPONSE_RESULT.containing_type = _GETASSETDIGESTRESPONSE
DESCRIPTOR.message_types_by_name['GetAssetDigestResponse'] = _GETASSETDIGESTRESPONSE

GetAssetDigestResponse = _reflection.GeneratedProtocolMessageType('GetAssetDigestResponse', (_message.Message,), dict(
  DESCRIPTOR = _GETASSETDIGESTRESPONSE,
  __module__ = 'pogoprotos.networking.responses.get_asset_digest_response_pb2'
  # @@protoc_insertion_point(class_scope:pogoprotos.networking.responses.GetAssetDigestResponse)
  ))
_sym_db.RegisterMessage(GetAssetDigestResponse)


# @@protoc_insertion_point(module_scope)