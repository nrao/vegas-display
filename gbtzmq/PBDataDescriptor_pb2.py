# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from google.protobuf import descriptor_pb2
from google.protobuf import message
from google.protobuf import reflection

# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2
from gbtzmq import TimeStamp_pb2

DESCRIPTOR = descriptor.FileDescriptor(
  name='PBDataDescriptor.proto',
  package='',
  serialized_pb='\n\x16PBDataDescriptor.proto\x1a google/protobuf/descriptor.proto\x1a\x0fTimeStamp.proto\"\xdd\x10\n\x0bPBDataField\x12\n\n\x02id\x18\x14 \x02(\x05\x12\x0c\n\x04name\x18\x15 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x16 \x01(\t\x12\x1f\n\x04type\x18\x17 \x02(\x0e\x32\x11.PBDataField.Type\x12\x11\n\tprecision\x18\x18 \x01(\x05\x12\x10\n\x08\x61\x63\x63uracy\x18\x19 \x01(\x05\x12%\n\x04unit\x18\x1a \x01(\x0e\x32\x11.PBDataField.Unit:\x04NONE\x12\x10\n\x08\x66itsname\x18\x1b \x01(\t\x12\x1f\n\ttimeStamp\x18\x1c \x01(\x0b\x32\x0c.pbTimeStamp\x12\x16\n\nval_double\x18\x01 \x03(\x01\x42\x02\x10\x01\x12\x15\n\tval_float\x18\x02 \x03(\x02\x42\x02\x10\x01\x12\x14\n\x08val_bool\x18\x03 \x03(\x08\x42\x02\x10\x01\x12\x12\n\nval_string\x18\x04 \x03(\t\x12\x11\n\tval_bytes\x18\x05 \x03(\x0c\x12\x15\n\tval_int32\x18\x06 \x03(\x05\x42\x02\x10\x01\x12\x15\n\tval_int64\x18\x07 \x03(\x03\x42\x02\x10\x01\x12\x16\n\nval_uint32\x18\x08 \x03(\rB\x02\x10\x01\x12\x16\n\nval_uint64\x18\t \x03(\x04\x42\x02\x10\x01\x12 \n\nval_struct\x18\n \x03(\x0b\x32\x0c.PBDataField\"x\n\x04Type\x12\n\n\x06\x44OUBLE\x10\x01\x12\t\n\x05\x46LOAT\x10\x02\x12\x08\n\x04\x42OOL\x10\x03\x12\n\n\x06STRING\x10\x04\x12\t\n\x05\x42YTES\x10\x05\x12\t\n\x05INT32\x10\x06\x12\t\n\x05INT64\x10\x07\x12\n\n\x06UINT32\x10\x08\x12\n\n\x06UINT64\x10\t\x12\n\n\x06STRUCT\x10\n\"\x98\x0c\n\x04Unit\x12\x12\n\x04NONE\x10\x00\x1a\x08\x82\xb5\x18\x04None\x12\x11\n\x06METERS\x10\x01\x1a\x05\x82\xb5\x18\x01m\x12\x17\n\x0bMICROMETERS\x10\x02\x1a\x06\x82\xb5\x18\x02um\x12\x17\n\x0bMILLIMETERS\x10\x03\x1a\x06\x82\xb5\x18\x02mm\x12\x17\n\x0b\x43\x45NTIMETERS\x10\x04\x1a\x06\x82\xb5\x18\x02\x63m\x12\x19\n\x0cSQUAREMETERS\x10\x05\x1a\x07\x82\xb5\x18\x03m^2\x12\x18\n\x0b\x43UBICMETERS\x10\x06\x1a\x07\x82\xb5\x18\x03m^3\x12\x19\n\x0cMETERSPERSEC\x10\x07\x1a\x07\x82\xb5\x18\x03m/s\x12\x16\n\x08KMPERSEC\x10\x08\x1a\x08\x82\xb5\x18\x04km/s\x12\x1c\n\rMETERSPERSEC2\x10\t\x1a\t\x82\xb5\x18\x05m/s^2\x12\x19\n\tKMPERSEC2\x10\n\x1a\n\x82\xb5\x18\x06km/s^2\x12\x1c\n\rMETERSPERSEC3\x10\x0b\x1a\t\x82\xb5\x18\x05m/s^3\x12\x19\n\tKMPERSEC3\x10\x0c\x1a\n\x82\xb5\x18\x06km/s^3\x12\x14\n\x07RADIANS\x10\r\x1a\x07\x82\xb5\x18\x03rad\x12\x14\n\x07\x44\x45GREES\x10\x0e\x1a\x07\x82\xb5\x18\x03\x64\x65g\x12\x1c\n\rRADIANSPERSEC\x10\x0f\x1a\t\x82\xb5\x18\x05rad/s\x12\x1c\n\rDEGREESPERSEC\x10\x10\x1a\t\x82\xb5\x18\x05\x64\x65g/s\x12\x1e\n\x0e\x44\x45GREESPERHOUR\x10\x11\x1a\n\x82\xb5\x18\x06\x64\x65g/hr\x12\x1f\n\x0eRADIANSPERSEC2\x10\x12\x1a\x0b\x82\xb5\x18\x07rad/s^2\x12\x1f\n\x0e\x44\x45GREESPERSEC2\x10\x13\x1a\x0b\x82\xb5\x18\x07\x64\x65g/s^2\x12 \n\x0f\x44\x45GREESPERHOUR2\x10\x14\x1a\x0b\x82\xb5\x18\x07\x64\x65g/h^2\x12\x1f\n\x0eRADIANSPERSEC3\x10\x15\x1a\x0b\x82\xb5\x18\x07rad/s^3\x12\x1f\n\x0e\x44\x45GREESPERSEC3\x10\x16\x1a\x0b\x82\xb5\x18\x07\x64\x65g/s^3\x12 \n\x0f\x44\x45GREESPERHOUR3\x10\x17\x1a\x0b\x82\xb5\x18\x07\x64\x65g/h^3\x12\x1a\n\nARCSECONDS\x10\x18\x1a\n\x82\xb5\x18\x06\x61rcsec\x12\x1a\n\nARCMINUTES\x10\x19\x1a\n\x82\xb5\x18\x06\x61rcmin\x12\x16\n\nSTERADIANS\x10\x1a\x1a\x06\x82\xb5\x18\x02sr\x12\x12\n\x07SECONDS\x10\x1b\x1a\x05\x82\xb5\x18\x01s\x12\x18\n\x0cMILLISECONDS\x10\x1c\x1a\x06\x82\xb5\x18\x02ms\x12\x18\n\x0cMICROSECONDS\x10\x1d\x1a\x06\x82\xb5\x18\x02us\x12\x17\n\x0bNANOSECONDS\x10\x1e\x1a\x06\x82\xb5\x18\x02ns\x12\x17\n\x0bPICOSECONDS\x10\x1f\x1a\x06\x82\xb5\x18\x02ps\x12\x14\n\x07MINUTES\x10 \x1a\x07\x82\xb5\x18\x03min\x12\x10\n\x05HOURS\x10!\x1a\x05\x82\xb5\x18\x01h\x12\x0f\n\x04\x44\x41YS\x10\"\x1a\x05\x82\xb5\x18\x01\x64\x12\x15\n\x06MONTHS\x10#\x1a\t\x82\xb5\x18\x05month\x12\x10\n\x05YEARS\x10$\x1a\x05\x82\xb5\x18\x01y\x12\x1c\n\tTIMESTAMP\x10%\x1a\r\x82\xb5\x18\ttimestamp\x12!\n\x10MINUTESPERMINUTE\x10&\x1a\x0b\x82\xb5\x18\x07min/min\x12$\n\x11MINUTESPERMINUTE2\x10\'\x1a\r\x82\xb5\x18\tmin/min^2\x12$\n\x11MINUTESPERMINUTE3\x10(\x1a\r\x82\xb5\x18\tmin/min^3\x12\x12\n\x07KELVINS\x10)\x1a\x05\x82\xb5\x18\x01K\x12\x12\n\x07\x43\x45LSIUS\x10*\x1a\x05\x82\xb5\x18\x01\x43\x12\x10\n\x05GRAMS\x10+\x1a\x05\x82\xb5\x18\x01g\x12\x11\n\x05HERTZ\x10,\x1a\x06\x82\xb5\x18\x02Hz\x12\x16\n\tKILOHERTZ\x10-\x1a\x07\x82\xb5\x18\x03KHz\x12\x16\n\tMEGAHERTZ\x10.\x1a\x07\x82\xb5\x18\x03MHz\x12\x16\n\tGIGAHERTZ\x10/\x1a\x07\x82\xb5\x18\x03GHz\x12\x10\n\x05VOLTS\x10\x30\x1a\x05\x82\xb5\x18\x01V\x12\x0f\n\x04\x41MPS\x10\x31\x1a\x05\x82\xb5\x18\x01\x41\x12\x15\n\tMILLIAMPS\x10\x32\x1a\x06\x82\xb5\x18\x02mA\x12\x10\n\x05WATTS\x10\x33\x1a\x05\x82\xb5\x18\x01W\x12\x16\n\nMICROWATTS\x10\x34\x1a\x06\x82\xb5\x18\x02mW\x12\x0e\n\x02\x44\x42\x10\x35\x1a\x06\x82\xb5\x18\x02\x64\x42\x12\x10\n\x03\x44\x42M\x10\x36\x1a\x07\x82\xb5\x18\x03\x64\x42m\x12\x10\n\x03PSI\x10\x37\x1a\x07\x82\xb5\x18\x03psi\x12\x13\n\x07PASCALS\x10\x38\x1a\x06\x82\xb5\x18\x02Pa\x12\x18\n\x0bKILOPASCALS\x10\x39\x1a\x07\x82\xb5\x18\x03KPa\x12\x15\n\tMILLIBARS\x10:\x1a\x06\x82\xb5\x18\x02mb\x12\x12\n\x04TORR\x10;\x1a\x08\x82\xb5\x18\x04Torr\x12\x1e\n\rPARSECSPERCM3\x10<\x1a\x0b\x82\xb5\x18\x07pc/cm^3\x12\x14\n\x05\x43OUNT\x10=\x1a\t\x82\xb5\x18\x05\x63ount:1\n\x04\x61\x62\x62r\x12!.google.protobuf.EnumValueOptions\x18\xd0\x86\x03 \x01(\t')


ABBR_FIELD_NUMBER = 50000
abbr = descriptor.FieldDescriptor(
  name='abbr', full_name='abbr', index=0,
  number=50000, type=9, cpp_type=9, label=1,
  has_default_value=False, default_value=unicode("", "utf-8"),
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)

_PBDATAFIELD_TYPE = descriptor.EnumDescriptor(
  name='Type',
  full_name='PBDataField.Type',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='DOUBLE', index=0, number=1,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='FLOAT', index=1, number=2,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BOOL', index=2, number=3,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STRING', index=3, number=4,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='BYTES', index=4, number=5,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='INT32', index=5, number=6,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='INT64', index=6, number=7,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UINT32', index=7, number=8,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='UINT64', index=8, number=9,
      options=None,
      type=None),
    descriptor.EnumValueDescriptor(
      name='STRUCT', index=9, number=10,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=536,
  serialized_end=656,
)

_PBDATAFIELD_UNIT = descriptor.EnumDescriptor(
  name='Unit',
  full_name='PBDataField.Unit',
  filename=None,
  file=DESCRIPTOR,
  values=[
    descriptor.EnumValueDescriptor(
      name='NONE', index=0, number=0,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\004None'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='METERS', index=1, number=1,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001m'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MICROMETERS', index=2, number=2,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002um'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MILLIMETERS', index=3, number=3,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002mm'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='CENTIMETERS', index=4, number=4,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002cm'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='SQUAREMETERS', index=5, number=5,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003m^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='CUBICMETERS', index=6, number=6,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003m^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='METERSPERSEC', index=7, number=7,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003m/s'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KMPERSEC', index=8, number=8,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\004km/s'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='METERSPERSEC2', index=9, number=9,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005m/s^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KMPERSEC2', index=10, number=10,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\006km/s^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='METERSPERSEC3', index=11, number=11,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005m/s^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KMPERSEC3', index=12, number=12,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\006km/s^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIANS', index=13, number=13,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003rad'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREES', index=14, number=14,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003deg'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIANSPERSEC', index=15, number=15,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005rad/s'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERSEC', index=16, number=16,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005deg/s'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERHOUR', index=17, number=17,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\006deg/hr'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIANSPERSEC2', index=18, number=18,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007rad/s^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERSEC2', index=19, number=19,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007deg/s^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERHOUR2', index=20, number=20,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007deg/h^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='RADIANSPERSEC3', index=21, number=21,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007rad/s^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERSEC3', index=22, number=22,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007deg/s^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DEGREESPERHOUR3', index=23, number=23,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007deg/h^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='ARCSECONDS', index=24, number=24,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\006arcsec'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='ARCMINUTES', index=25, number=25,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\006arcmin'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='STERADIANS', index=26, number=26,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002sr'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='SECONDS', index=27, number=27,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001s'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MILLISECONDS', index=28, number=28,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002ms'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MICROSECONDS', index=29, number=29,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002us'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='NANOSECONDS', index=30, number=30,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002ns'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='PICOSECONDS', index=31, number=31,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002ps'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MINUTES', index=32, number=32,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003min'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='HOURS', index=33, number=33,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001h'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DAYS', index=34, number=34,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001d'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MONTHS', index=35, number=35,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005month'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='YEARS', index=36, number=36,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001y'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='TIMESTAMP', index=37, number=37,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\ttimestamp'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MINUTESPERMINUTE', index=38, number=38,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007min/min'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MINUTESPERMINUTE2', index=39, number=39,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\tmin/min^2'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MINUTESPERMINUTE3', index=40, number=40,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\tmin/min^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KELVINS', index=41, number=41,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001K'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='CELSIUS', index=42, number=42,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001C'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='GRAMS', index=43, number=43,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001g'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='HERTZ', index=44, number=44,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002Hz'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KILOHERTZ', index=45, number=45,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003KHz'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MEGAHERTZ', index=46, number=46,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003MHz'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='GIGAHERTZ', index=47, number=47,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003GHz'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='VOLTS', index=48, number=48,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001V'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='AMPS', index=49, number=49,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001A'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MILLIAMPS', index=50, number=50,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002mA'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='WATTS', index=51, number=51,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\001W'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MICROWATTS', index=52, number=52,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002mW'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DB', index=53, number=53,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002dB'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='DBM', index=54, number=54,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003dBm'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='PSI', index=55, number=55,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003psi'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='PASCALS', index=56, number=56,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002Pa'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='KILOPASCALS', index=57, number=57,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\003KPa'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='MILLIBARS', index=58, number=58,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\002mb'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='TORR', index=59, number=59,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\004Torr'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='PARSECSPERCM3', index=60, number=60,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\007pc/cm^3'),
      type=None),
    descriptor.EnumValueDescriptor(
      name='COUNT', index=61, number=61,
      options=descriptor._ParseOptions(descriptor_pb2.EnumValueOptions(), '\202\265\030\005count'),
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=659,
  serialized_end=2219,
)


_PBDATAFIELD = descriptor.Descriptor(
  name='PBDataField',
  full_name='PBDataField',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    descriptor.FieldDescriptor(
      name='id', full_name='PBDataField.id', index=0,
      number=20, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='name', full_name='PBDataField.name', index=1,
      number=21, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='description', full_name='PBDataField.description', index=2,
      number=22, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='type', full_name='PBDataField.type', index=3,
      number=23, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='precision', full_name='PBDataField.precision', index=4,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='accuracy', full_name='PBDataField.accuracy', index=5,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='unit', full_name='PBDataField.unit', index=6,
      number=26, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='fitsname', full_name='PBDataField.fitsname', index=7,
      number=27, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='timeStamp', full_name='PBDataField.timeStamp', index=8,
      number=28, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_double', full_name='PBDataField.val_double', index=9,
      number=1, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_float', full_name='PBDataField.val_float', index=10,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_bool', full_name='PBDataField.val_bool', index=11,
      number=3, type=8, cpp_type=7, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_string', full_name='PBDataField.val_string', index=12,
      number=4, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_bytes', full_name='PBDataField.val_bytes', index=13,
      number=5, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    descriptor.FieldDescriptor(
      name='val_int32', full_name='PBDataField.val_int32', index=14,
      number=6, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_int64', full_name='PBDataField.val_int64', index=15,
      number=7, type=3, cpp_type=2, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_uint32', full_name='PBDataField.val_uint32', index=16,
      number=8, type=13, cpp_type=3, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_uint64', full_name='PBDataField.val_uint64', index=17,
      number=9, type=4, cpp_type=4, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=descriptor._ParseOptions(descriptor_pb2.FieldOptions(), '\020\001')),
    descriptor.FieldDescriptor(
      name='val_struct', full_name='PBDataField.val_struct', index=18,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PBDATAFIELD_TYPE,
    _PBDATAFIELD_UNIT,
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=78,
  serialized_end=2219,
)

_PBDATAFIELD.fields_by_name['type'].enum_type = _PBDATAFIELD_TYPE
_PBDATAFIELD.fields_by_name['unit'].enum_type = _PBDATAFIELD_UNIT
_PBDATAFIELD.fields_by_name['timeStamp'].message_type = TimeStamp_pb2._PBTIMESTAMP
_PBDATAFIELD.fields_by_name['val_struct'].message_type = _PBDATAFIELD
_PBDATAFIELD_TYPE.containing_type = _PBDATAFIELD;
_PBDATAFIELD_UNIT.containing_type = _PBDATAFIELD;
DESCRIPTOR.message_types_by_name['PBDataField'] = _PBDATAFIELD

class PBDataField(message.Message):
  __metaclass__ = reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _PBDATAFIELD
  
  # @@protoc_insertion_point(class_scope:PBDataField)

google.protobuf.descriptor_pb2.EnumValueOptions.RegisterExtension(abbr)
# @@protoc_insertion_point(module_scope)
