"""
This is the mapping between the Python driver and the compiled library data
type. The 0th index of the `_fields_` tuples maps the Python declaration to
the data type (like `c_float`) and the position of that attribute in the memory
of the object. The order itself as defined in `_fields_` maps the location in
memory to the Fortran type. In this case, the Fortran type is

    type, bind(C) :: Vec3
        real(kind=c_float) :: x1
        real(kind=c_float) :: x2
        real(kind=c_float) :: x3
    end type

When the order of the `Structure` object matches the order of the type
as defined in Fortran, the data is passed correctly. However, if the
attributes are in a different order, then the memory location passed
to Fortran is not interpreted correctly. In the case of the Vec3 class,
all attributes are of the same size, so they can be mixed up and the data
will still be unpacked, though out of order. If there are different sized
attributes (c_float, c_int, ...), then defining these out of order will
cause strange behavior when the Fortran routines try to read the data.

Args:
    Structure ([type]): [description]
"""

from ctypes import (
    POINTER,
    Structure,
    byref,
    c_int,
    c_float,
    c_double,
    c_char,
)

class Vec3(Structure):
	_fields_ = [
    	("x1", c_float),
    	("x3", c_float),
    	("x2", c_float),
	]

class Strings(Structure):
    _fields_ = [
        ("string8", c_char * 8),
        ("string1024", c_char * 1024)
    ]

class Arrays(Structure):
    _fields_ = [
        ("one_by_two", c_float * 2)
    ]
