# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: foundation/protos/ocr/types.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from foundation.protos import geometry_pb2 as foundation_dot_protos_dot_geometry__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='foundation/protos/ocr/types.proto',
  package='ocr',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n!foundation/protos/ocr/types.proto\x12\x03ocr\x1a foundation/protos/geometry.proto\"\xbd\x01\n\tInputWord\x12$\n\x0c\x62ounding_box\x18\x01 \x02(\x0b\x32\x0e.geometry.BBox\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\'\n\nconfidence\x18\x06 \x01(\x0b\x32\x13.ocr.WordConfidence\x12\x13\n\x0bline_height\x18\x07 \x01(\x02\x12\x12\n\nword_width\x18\x08 \x01(\x02\x12\x12\n\nchar_width\x18\t \x01(\x02\x12\x16\n\x0erotation_angle\x18\n \x01(\x02\"p\n\x0eWordConfidence\x12\x17\n\x0fword_confidence\x18\x01 \x01(\x01\x12\x16\n\x0elow_confidence\x18\x02 \x01(\x08\x12-\n\x10\x63har_confidences\x18\x03 \x03(\x0b\x32\x13.ocr.CharConfidence\"4\n\x0e\x43harConfidence\x12\x12\n\npercentage\x18\x01 \x02(\x01\x12\x0e\n\x06unsure\x18\x02 \x01(\x08'
  ,
  dependencies=[foundation_dot_protos_dot_geometry__pb2.DESCRIPTOR,])




_INPUTWORD = _descriptor.Descriptor(
  name='InputWord',
  full_name='ocr.InputWord',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='bounding_box', full_name='ocr.InputWord.bounding_box', index=0,
      number=1, type=11, cpp_type=10, label=2,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='text', full_name='ocr.InputWord.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='confidence', full_name='ocr.InputWord.confidence', index=2,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='line_height', full_name='ocr.InputWord.line_height', index=3,
      number=7, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='word_width', full_name='ocr.InputWord.word_width', index=4,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='char_width', full_name='ocr.InputWord.char_width', index=5,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='rotation_angle', full_name='ocr.InputWord.rotation_angle', index=6,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=77,
  serialized_end=266,
)


_WORDCONFIDENCE = _descriptor.Descriptor(
  name='WordConfidence',
  full_name='ocr.WordConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='word_confidence', full_name='ocr.WordConfidence.word_confidence', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='low_confidence', full_name='ocr.WordConfidence.low_confidence', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='char_confidences', full_name='ocr.WordConfidence.char_confidences', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=268,
  serialized_end=380,
)


_CHARCONFIDENCE = _descriptor.Descriptor(
  name='CharConfidence',
  full_name='ocr.CharConfidence',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='percentage', full_name='ocr.CharConfidence.percentage', index=0,
      number=1, type=1, cpp_type=5, label=2,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='unsure', full_name='ocr.CharConfidence.unsure', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=382,
  serialized_end=434,
)

_INPUTWORD.fields_by_name['bounding_box'].message_type = foundation_dot_protos_dot_geometry__pb2._BBOX
_INPUTWORD.fields_by_name['confidence'].message_type = _WORDCONFIDENCE
_WORDCONFIDENCE.fields_by_name['char_confidences'].message_type = _CHARCONFIDENCE
DESCRIPTOR.message_types_by_name['InputWord'] = _INPUTWORD
DESCRIPTOR.message_types_by_name['WordConfidence'] = _WORDCONFIDENCE
DESCRIPTOR.message_types_by_name['CharConfidence'] = _CHARCONFIDENCE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InputWord = _reflection.GeneratedProtocolMessageType('InputWord', (_message.Message,), {
  'DESCRIPTOR' : _INPUTWORD,
  '__module__' : 'foundation.protos.ocr.types_pb2'
  # @@protoc_insertion_point(class_scope:ocr.InputWord)
  })
_sym_db.RegisterMessage(InputWord)

WordConfidence = _reflection.GeneratedProtocolMessageType('WordConfidence', (_message.Message,), {
  'DESCRIPTOR' : _WORDCONFIDENCE,
  '__module__' : 'foundation.protos.ocr.types_pb2'
  # @@protoc_insertion_point(class_scope:ocr.WordConfidence)
  })
_sym_db.RegisterMessage(WordConfidence)

CharConfidence = _reflection.GeneratedProtocolMessageType('CharConfidence', (_message.Message,), {
  'DESCRIPTOR' : _CHARCONFIDENCE,
  '__module__' : 'foundation.protos.ocr.types_pb2'
  # @@protoc_insertion_point(class_scope:ocr.CharConfidence)
  })
_sym_db.RegisterMessage(CharConfidence)


# @@protoc_insertion_point(module_scope)
