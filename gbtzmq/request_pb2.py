# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import message
from google.protobuf import reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='request.proto',
  package='',
  serialized_pb='\n\rrequest.proto\x1a google/protobuf/descriptor.proto\"\xf3\x01\n\x10PBRequestService\x12\x13\n\x0bpublish_url\x18\x01 \x03(\t\x12\x14\n\x0csnapshot_url\x18\x02 \x03(\t\x12\x13\n\x0b\x63ontrol_url\x18\x03 \x03(\t\x12\x0c\n\x04host\x18\x13 \x01(\t\x12\r\n\x05major\x18\x14 \x02(\t\x12\r\n\x05minor\x18\x15 \x02(\t\x12.\n\tinterface\x18\x16 \x01(\x0e\x32\x1b.PBRequestService.Interface\x12\x0e\n\x06\x65rrors\x18\x17 \x01(\x05\"3\n\tInterface\x12\x0b\n\x07PUBLISH\x10\x00\x12\x0c\n\x08SNAPSHOT\x10\x01\x12\x0b\n\x07\x43ONTROL\x10\x02')



_PBREQUESTSERVICE_INTERFACE = descriptor.EnumDescriptor(
  name='Interface',
  full_name='PBRequestService.Interface',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='PUBLISH', index=0, number=0,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='SNAPSHOT', index=1, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='CONTROL', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=244,
  serialized_end=295,
)


_PBREQUESTSERVICE = descriptor.Descriptor(
  name='PBRequestService',
  full_name='PBRequestService',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='publish_url', full_name='PBRequestService.publish_url', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='snapshot_url', full_name='PBRequestService.snapshot_url', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='control_url', full_name='PBRequestService.control_url', index=2,
      number=3, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='host', full_name='PBRequestService.host', index=3,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='major', full_name='PBRequestService.major', index=4,
      number=20, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='minor', full_name='PBRequestService.minor', index=5,
      number=21, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='interface', full_name='PBRequestService.interface', index=6,
      number=22, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='errors', full_name='PBRequestService.errors', index=7,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBREQUESTSERVICE_INTERFACE,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=52,
  serialized_end=295,
)

_PBREQUESTSERVICE.fields_by_name['interface'].enum_type = _PBREQUESTSERVICE_INTERFACE
_PBREQUESTSERVICE_INTERFACE.containing_type = _PBREQUESTSERVICE;
DESCRIPTOR.message_types_by_name['PBRequestService'] = _PBREQUESTSERVICE

class PBRequestService(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBREQUESTSERVICE
  
  # @@protoc_insertion_point(class_scope:PBRequestService)

# @@protoc_insertion_point(module_scope)