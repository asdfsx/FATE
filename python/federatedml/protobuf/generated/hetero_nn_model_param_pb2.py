# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: hetero-nn-model-param.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='hetero-nn-model-param.proto',
  package='com.webank.ai.fate.core.mlmodel.buffer',
  syntax='proto3',
  serialized_options=_b('B\027HeteroNNModelParamProto'),
  serialized_pb=_b('\n\x1bhetero-nn-model-param.proto\x12&com.webank.ai.fate.core.mlmodel.buffer\"\xb8\x01\n\x15InteractiveLayerParam\x12\x11\n\tacc_noise\x18\x01 \x01(\x0c\x12+\n#interactive_guest_saved_model_bytes\x18\x02 \x01(\x0c\x12*\n\"interactive_host_saved_model_bytes\x18\x03 \x03(\x0c\x12\x18\n\x10host_input_shape\x18\x04 \x03(\x05\x12\x19\n\x11guest_input_shape\x18\x05 \x01(\x05\"\x9c\x02\n\x12HeteroNNModelParam\x12 \n\x18\x62ottom_saved_model_bytes\x18\x01 \x01(\x0c\x12^\n\x17interactive_layer_param\x18\x02 \x01(\x0b\x32=.com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam\x12\x1d\n\x15top_saved_model_bytes\x18\x03 \x01(\x0c\x12\x10\n\x08is_empty\x18\x04 \x01(\x08\x12 \n\x18\x62ottom_model_input_shape\x18\x05 \x01(\x05\x12\x1d\n\x15top_model_input_shape\x18\x06 \x01(\x05\x12\x12\n\ncoae_bytes\x18\x07 \x01(\x0c\"\xe5\x01\n\rHeteroNNParam\x12Y\n\x15hetero_nn_model_param\x18\x01 \x01(\x0b\x32:.com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam\x12\x12\n\niter_epoch\x18\x02 \x01(\x05\x12\x14\n\x0chistory_loss\x18\x03 \x03(\x01\x12\x14\n\x0cis_converged\x18\x04 \x01(\x08\x12\x0e\n\x06header\x18\x05 \x03(\t\x12\x11\n\tnum_label\x18\x06 \x01(\x05\x12\x16\n\x0e\x62\x65st_iteration\x18\x07 \x01(\x05\x42\x19\x42\x17HeteroNNModelParamProtob\x06proto3')
)




_INTERACTIVELAYERPARAM = _descriptor.Descriptor(
  name='InteractiveLayerParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='acc_noise', full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam.acc_noise', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive_guest_saved_model_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam.interactive_guest_saved_model_bytes', index=1,
      number=2, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive_host_saved_model_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam.interactive_host_saved_model_bytes', index=2,
      number=3, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='host_input_shape', full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam.host_input_shape', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='guest_input_shape', full_name='com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam.guest_input_shape', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=72,
  serialized_end=256,
)


_HETERONNMODELPARAM = _descriptor.Descriptor(
  name='HeteroNNModelParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='bottom_saved_model_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.bottom_saved_model_bytes', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='interactive_layer_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.interactive_layer_param', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_saved_model_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.top_saved_model_bytes', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_empty', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.is_empty', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bottom_model_input_shape', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.bottom_model_input_shape', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='top_model_input_shape', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.top_model_input_shape', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='coae_bytes', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam.coae_bytes', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
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
  serialized_start=259,
  serialized_end=543,
)


_HETERONNPARAM = _descriptor.Descriptor(
  name='HeteroNNParam',
  full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='hetero_nn_model_param', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.hetero_nn_model_param', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='iter_epoch', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.iter_epoch', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='history_loss', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.history_loss', index=2,
      number=3, type=1, cpp_type=5, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='is_converged', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.is_converged', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='header', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.header', index=4,
      number=5, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='num_label', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.num_label', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='best_iteration', full_name='com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam.best_iteration', index=6,
      number=7, type=5, cpp_type=1, label=1,
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
  serialized_start=546,
  serialized_end=775,
)

_HETERONNMODELPARAM.fields_by_name['interactive_layer_param'].message_type = _INTERACTIVELAYERPARAM
_HETERONNPARAM.fields_by_name['hetero_nn_model_param'].message_type = _HETERONNMODELPARAM
DESCRIPTOR.message_types_by_name['InteractiveLayerParam'] = _INTERACTIVELAYERPARAM
DESCRIPTOR.message_types_by_name['HeteroNNModelParam'] = _HETERONNMODELPARAM
DESCRIPTOR.message_types_by_name['HeteroNNParam'] = _HETERONNPARAM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

InteractiveLayerParam = _reflection.GeneratedProtocolMessageType('InteractiveLayerParam', (_message.Message,), {
  'DESCRIPTOR' : _INTERACTIVELAYERPARAM,
  '__module__' : 'hetero_nn_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.InteractiveLayerParam)
  })
_sym_db.RegisterMessage(InteractiveLayerParam)

HeteroNNModelParam = _reflection.GeneratedProtocolMessageType('HeteroNNModelParam', (_message.Message,), {
  'DESCRIPTOR' : _HETERONNMODELPARAM,
  '__module__' : 'hetero_nn_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.HeteroNNModelParam)
  })
_sym_db.RegisterMessage(HeteroNNModelParam)

HeteroNNParam = _reflection.GeneratedProtocolMessageType('HeteroNNParam', (_message.Message,), {
  'DESCRIPTOR' : _HETERONNPARAM,
  '__module__' : 'hetero_nn_model_param_pb2'
  # @@protoc_insertion_point(class_scope:com.webank.ai.fate.core.mlmodel.buffer.HeteroNNParam)
  })
_sym_db.RegisterMessage(HeteroNNParam)


DESCRIPTOR._options = None
# @@protoc_insertion_point(module_scope)
