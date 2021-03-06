# This Python file uses the following encoding: utf-8
"""autogenerated by genpy from posInfo/PositionInfo_M.msg. Do not edit."""
import codecs
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class PositionInfo_M(genpy.Message):
  _md5sum = "b4b81b197fe93582c1d4236893d83fff"
  _type = "posInfo/PositionInfo_M"
  _has_header = False  # flag to mark the presence of a Header object
  _full_text = """uint8 ret
float32 vx
float32 vy
float32 vz
float32 px
float32 py
float32 pz

uint8 ok = 1
uint8 err = 0
"""
  # Pseudo-constants
  ok = 1
  err = 0

  __slots__ = ['ret','vx','vy','vz','px','py','pz']
  _slot_types = ['uint8','float32','float32','float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       ret,vx,vy,vz,px,py,pz

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(PositionInfo_M, self).__init__(*args, **kwds)
      # message fields cannot be None, assign default values for those that are
      if self.ret is None:
        self.ret = 0
      if self.vx is None:
        self.vx = 0.
      if self.vy is None:
        self.vy = 0.
      if self.vz is None:
        self.vz = 0.
      if self.px is None:
        self.px = 0.
      if self.py is None:
        self.py = 0.
      if self.pz is None:
        self.pz = 0.
    else:
      self.ret = 0
      self.vx = 0.
      self.vy = 0.
      self.vz = 0.
      self.px = 0.
      self.py = 0.
      self.pz = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_get_struct_B6f().pack(_x.ret, _x.vx, _x.vy, _x.vz, _x.px, _x.py, _x.pz))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.ret, _x.vx, _x.vy, _x.vz, _x.px, _x.py, _x.pz,) = _get_struct_B6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_get_struct_B6f().pack(_x.ret, _x.vx, _x.vy, _x.vz, _x.px, _x.py, _x.pz))
    except struct.error as se: self._check_types(struct.error("%s: '%s' when writing '%s'" % (type(se), str(se), str(locals().get('_x', self)))))
    except TypeError as te: self._check_types(ValueError("%s: '%s' when writing '%s'" % (type(te), str(te), str(locals().get('_x', self)))))

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    codecs.lookup_error("rosmsg").msg_type = self._type
    try:
      end = 0
      _x = self
      start = end
      end += 25
      (_x.ret, _x.vx, _x.vy, _x.vz, _x.px, _x.py, _x.pz,) = _get_struct_B6f().unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e)  # most likely buffer underfill

_struct_I = genpy.struct_I
def _get_struct_I():
    global _struct_I
    return _struct_I
_struct_B6f = None
def _get_struct_B6f():
    global _struct_B6f
    if _struct_B6f is None:
        _struct_B6f = struct.Struct("<B6f")
    return _struct_B6f
