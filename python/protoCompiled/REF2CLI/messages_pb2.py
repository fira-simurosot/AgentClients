# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: REF2CLI/messages.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import common_pb2 as common__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='REF2CLI/messages.proto',
  package='fira_message.ref_to_cli',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x16REF2CLI/messages.proto\x12\x17\x66ira_message.ref_to_cli\x1a\x0c\x63ommon.proto\"\x18\n\x08TeamName\x12\x0c\n\x04name\x18\x01 \x01(\t\"9\n\x08TeamInfo\x12-\n\x05\x63olor\x18\x01 \x01(\x0e\x32\x1e.fira_message.ref_to_cli.Color\"-\n\x06Robots\x12#\n\x06robots\x18\x01 \x03(\x0b\x32\x13.fira_message.Robot\"f\n\x0b\x45nvironment\x12\"\n\x05\x66rame\x18\x01 \x01(\x0b\x32\x13.fira_message.Frame\x12\x33\n\x08\x66oulInfo\x18\x04 \x01(\x0b\x32!.fira_message.ref_to_cli.FoulInfo\"\xb5\x03\n\x08\x46oulInfo\x12:\n\x05phase\x18\x01 \x01(\x0e\x32+.fira_message.ref_to_cli.FoulInfo.PhaseType\x12\x38\n\x04type\x18\x02 \x01(\x0e\x32*.fira_message.ref_to_cli.FoulInfo.FoulType\x12,\n\x05\x61\x63tor\x18\x03 \x01(\x0e\x32\x1d.fira_message.ref_to_cli.Side\"\xa8\x01\n\x08\x46oulType\x12\n\n\x06PlayOn\x10\x00\x12\r\n\tPlaceKick\x10\x03\x12\x0f\n\x0bPenaltyKick\x10\x04\x12\x0c\n\x08\x46reeKick\x10\x05\x12\x0c\n\x08GoalKick\x10\x06\x12\x13\n\x0f\x46reeBallLeftTop\x10\x07\x12\x14\n\x10\x46reeBallRightTop\x10\x08\x12\x13\n\x0f\x46reeBallLeftBot\x10\t\x12\x14\n\x10\x46reeBallRightBot\x10\n\"Z\n\tPhaseType\x12\r\n\tFirstHalf\x10\x00\x12\x0e\n\nSecondHalf\x10\x01\x12\x0c\n\x08Overtime\x10\x02\x12\x13\n\x0fPenaltyShootout\x10\x03\x12\x0b\n\x07Stopped\x10\x04\";\n\nWheelSpeed\x12\x10\n\x08robot_id\x18\x01 \x01(\x05\x12\r\n\x05right\x18\x02 \x01(\x02\x12\x0c\n\x04left\x18\x03 \x01(\x02\">\n\x07\x43ommand\x12\x33\n\x06wheels\x18\x01 \x03(\x0b\x32#.fira_message.ref_to_cli.WheelSpeed*\x15\n\x05\x43olor\x12\x05\n\x01Y\x10\x00\x12\x05\n\x01\x42\x10\x01*\x1e\n\x04Side\x12\x08\n\x04Self\x10\x00\x12\x0c\n\x08Opponent\x10\x01\x62\x06proto3'
  ,
  dependencies=[common__pb2.DESCRIPTOR,])

_COLOR = _descriptor.EnumDescriptor(
  name='Color',
  full_name='fira_message.ref_to_cli.Color',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Y', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='B', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=866,
  serialized_end=887,
)
_sym_db.RegisterEnumDescriptor(_COLOR)

Color = enum_type_wrapper.EnumTypeWrapper(_COLOR)
_SIDE = _descriptor.EnumDescriptor(
  name='Side',
  full_name='fira_message.ref_to_cli.Side',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='Self', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Opponent', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=889,
  serialized_end=919,
)
_sym_db.RegisterEnumDescriptor(_SIDE)

Side = enum_type_wrapper.EnumTypeWrapper(_SIDE)
Y = 0
B = 1
Self = 0
Opponent = 1


_FOULINFO_FOULTYPE = _descriptor.EnumDescriptor(
  name='FoulType',
  full_name='fira_message.ref_to_cli.FoulInfo.FoulType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PlayOn', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PlaceKick', index=1, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PenaltyKick', index=2, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FreeKick', index=3, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='GoalKick', index=4, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FreeBallLeftTop', index=5, number=7,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FreeBallRightTop', index=6, number=8,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FreeBallLeftBot', index=7, number=9,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FreeBallRightBot', index=8, number=10,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=479,
  serialized_end=647,
)
_sym_db.RegisterEnumDescriptor(_FOULINFO_FOULTYPE)

_FOULINFO_PHASETYPE = _descriptor.EnumDescriptor(
  name='PhaseType',
  full_name='fira_message.ref_to_cli.FoulInfo.PhaseType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FirstHalf', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SecondHalf', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Overtime', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PenaltyShootout', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='Stopped', index=4, number=4,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=649,
  serialized_end=739,
)
_sym_db.RegisterEnumDescriptor(_FOULINFO_PHASETYPE)


_TEAMNAME = _descriptor.Descriptor(
  name='TeamName',
  full_name='fira_message.ref_to_cli.TeamName',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='fira_message.ref_to_cli.TeamName.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=89,
)


_TEAMINFO = _descriptor.Descriptor(
  name='TeamInfo',
  full_name='fira_message.ref_to_cli.TeamInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='color', full_name='fira_message.ref_to_cli.TeamInfo.color', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=91,
  serialized_end=148,
)


_ROBOTS = _descriptor.Descriptor(
  name='Robots',
  full_name='fira_message.ref_to_cli.Robots',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robots', full_name='fira_message.ref_to_cli.Robots.robots', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=150,
  serialized_end=195,
)


_ENVIRONMENT = _descriptor.Descriptor(
  name='Environment',
  full_name='fira_message.ref_to_cli.Environment',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='frame', full_name='fira_message.ref_to_cli.Environment.frame', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='foulInfo', full_name='fira_message.ref_to_cli.Environment.foulInfo', index=1,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=197,
  serialized_end=299,
)


_FOULINFO = _descriptor.Descriptor(
  name='FoulInfo',
  full_name='fira_message.ref_to_cli.FoulInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='phase', full_name='fira_message.ref_to_cli.FoulInfo.phase', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='type', full_name='fira_message.ref_to_cli.FoulInfo.type', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actor', full_name='fira_message.ref_to_cli.FoulInfo.actor', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _FOULINFO_FOULTYPE,
    _FOULINFO_PHASETYPE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=302,
  serialized_end=739,
)


_WHEELSPEED = _descriptor.Descriptor(
  name='WheelSpeed',
  full_name='fira_message.ref_to_cli.WheelSpeed',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='robot_id', full_name='fira_message.ref_to_cli.WheelSpeed.robot_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='right', full_name='fira_message.ref_to_cli.WheelSpeed.right', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='left', full_name='fira_message.ref_to_cli.WheelSpeed.left', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=741,
  serialized_end=800,
)


_COMMAND = _descriptor.Descriptor(
  name='Command',
  full_name='fira_message.ref_to_cli.Command',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='wheels', full_name='fira_message.ref_to_cli.Command.wheels', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=802,
  serialized_end=864,
)

_TEAMINFO.fields_by_name['color'].enum_type = _COLOR
_ROBOTS.fields_by_name['robots'].message_type = common__pb2._ROBOT
_ENVIRONMENT.fields_by_name['frame'].message_type = common__pb2._FRAME
_ENVIRONMENT.fields_by_name['foulInfo'].message_type = _FOULINFO
_FOULINFO.fields_by_name['phase'].enum_type = _FOULINFO_PHASETYPE
_FOULINFO.fields_by_name['type'].enum_type = _FOULINFO_FOULTYPE
_FOULINFO.fields_by_name['actor'].enum_type = _SIDE
_FOULINFO_FOULTYPE.containing_type = _FOULINFO
_FOULINFO_PHASETYPE.containing_type = _FOULINFO
_COMMAND.fields_by_name['wheels'].message_type = _WHEELSPEED
DESCRIPTOR.message_types_by_name['TeamName'] = _TEAMNAME
DESCRIPTOR.message_types_by_name['TeamInfo'] = _TEAMINFO
DESCRIPTOR.message_types_by_name['Robots'] = _ROBOTS
DESCRIPTOR.message_types_by_name['Environment'] = _ENVIRONMENT
DESCRIPTOR.message_types_by_name['FoulInfo'] = _FOULINFO
DESCRIPTOR.message_types_by_name['WheelSpeed'] = _WHEELSPEED
DESCRIPTOR.message_types_by_name['Command'] = _COMMAND
DESCRIPTOR.enum_types_by_name['Color'] = _COLOR
DESCRIPTOR.enum_types_by_name['Side'] = _SIDE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

TeamName = _reflection.GeneratedProtocolMessageType('TeamName', (_message.Message,), {
  'DESCRIPTOR' : _TEAMNAME,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.TeamName)
  })
_sym_db.RegisterMessage(TeamName)

TeamInfo = _reflection.GeneratedProtocolMessageType('TeamInfo', (_message.Message,), {
  'DESCRIPTOR' : _TEAMINFO,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.TeamInfo)
  })
_sym_db.RegisterMessage(TeamInfo)

Robots = _reflection.GeneratedProtocolMessageType('Robots', (_message.Message,), {
  'DESCRIPTOR' : _ROBOTS,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.Robots)
  })
_sym_db.RegisterMessage(Robots)

Environment = _reflection.GeneratedProtocolMessageType('Environment', (_message.Message,), {
  'DESCRIPTOR' : _ENVIRONMENT,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.Environment)
  })
_sym_db.RegisterMessage(Environment)

FoulInfo = _reflection.GeneratedProtocolMessageType('FoulInfo', (_message.Message,), {
  'DESCRIPTOR' : _FOULINFO,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.FoulInfo)
  })
_sym_db.RegisterMessage(FoulInfo)

WheelSpeed = _reflection.GeneratedProtocolMessageType('WheelSpeed', (_message.Message,), {
  'DESCRIPTOR' : _WHEELSPEED,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.WheelSpeed)
  })
_sym_db.RegisterMessage(WheelSpeed)

Command = _reflection.GeneratedProtocolMessageType('Command', (_message.Message,), {
  'DESCRIPTOR' : _COMMAND,
  '__module__' : 'REF2CLI.messages_pb2'
  # @@protoc_insertion_point(class_scope:fira_message.ref_to_cli.Command)
  })
_sym_db.RegisterMessage(Command)


# @@protoc_insertion_point(module_scope)
