# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: prime_numbers.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='prime_numbers.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=b'\n\x13prime_numbers.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x05\x32:\n\x14PrimeNumbersStreamer\x12\"\n\nget_primes\x12\x07.Number\x1a\x07.Number\"\x00\x30\x01\x62\x06proto3'
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=5, cpp_type=1, label=1,
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
  serialized_start=23,
  serialized_end=46,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'prime_numbers_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)



_PRIMENUMBERSSTREAMER = _descriptor.ServiceDescriptor(
  name='PrimeNumbersStreamer',
  full_name='PrimeNumbersStreamer',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=48,
  serialized_end=106,
  methods=[
  _descriptor.MethodDescriptor(
    name='get_primes',
    full_name='PrimeNumbersStreamer.get_primes',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_PRIMENUMBERSSTREAMER)

DESCRIPTOR.services_by_name['PrimeNumbersStreamer'] = _PRIMENUMBERSSTREAMER

# @@protoc_insertion_point(module_scope)
