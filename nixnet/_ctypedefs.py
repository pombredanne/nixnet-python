"""
Definition of types for calling into NI-XNET.

Distinct types (rather than aliases) are used to allow more accurate type
checking.
"""


from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import ctypes


class char(ctypes.c_char):  # NOQA: N801
    pass


class bool32(ctypes.c_uint):  # NOQA: N801
    """32-bit boolean C-type.

    For this to be as transparent as possible, b.value is not settable.
    """

    @property
    def value(self):
        return bool(super(bool32, self).value)

    @classmethod
    def from_param(cls, param):
        return ctypes.c_uint16(1) if bool(param) else ctypes.c_uint16(0)


class i8(ctypes.c_byte):  # NOQA: N801
    pass


class i16(ctypes.c_short):  # NOQA: N801
    pass


class i32(ctypes.c_int):  # NOQA: N801
    pass


class i64(ctypes.c_longlong):  # NOQA: N801
    pass


class u8(ctypes.c_ubyte):  # NOQA: N801
    pass


class u16(ctypes.c_ushort):  # NOQA: N801
    pass


class u32(ctypes.c_uint):  # NOQA: N801
    pass


class u64(ctypes.c_ulonglong):  # NOQA: N801
    pass


class f32(ctypes.c_float):  # NOQA: N801
    pass


class f64(ctypes.c_double):  # NOQA: N801
    pass


class nxVoidPtr(ctypes.c_void_p):  # NOQA: N801
    pass


class nxSessionRef_t(u32):  # NOQA: N801
    pass


class nxDatabaseRef_t(u32):  # NOQA: N801
    pass


class nxStatus_t(i32):  # NOQA: N801
    pass


class nxTimeStamp_t(u64):  # NOQA: N801
    pass


class nxFlexRayStats_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("NumSyntaxErrorChA", u32),
        ("NumSyntaxErrorChB", u32),
        ("NumContextErrorChB", u32),
        ("NumContextErrorChB", u32),
        ("NumSlotBoundaryViolationChB", u32),
        ("NumSlotBoundaryViolationChB", u32)]


class nxJ1939CommState_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("PGN", u32),
        ("SourceAddress", u8),
        ("DestinationAddress", u8),
        ("TransmitError", u8),
        ("ReceiveError", u8),
        ("Reserved1", u32),
        ("Reserved2", u32)]


class nxFrameFixed_t(ctypes.Structure):  # NOQA: N801
    _fields_ = [
        ("Timestamp", nxTimeStamp_t),
        ("Identifier", u32),
        ("Type", u8),
        ("Flags", u8),
        ("Info", u8)]


class nxFrameCAN_t(nxFrameFixed_t):  # NOQA: N801
    _fields_ = [
        ("PayloadLength", u8),
        ("Payload", u8 * 8)]


class nxFrameLIN_t(nxFrameFixed_t):  # NOQA: N801
    _fields_ = [
        ("PayloadLength", u8),
        ("Payload", u8 * 8)]


class nxFrameVar_t(nxFrameFixed_t):  # NOQA: N801
    _fields_ = [
        ("PayloadLength", u8),
        ("Payload", u8 * 8)]
