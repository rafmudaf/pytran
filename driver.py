
import numpy as np
from ctypes import CDLL, POINTER, c_int, c_float
import pythontypes

fortranlib = CDLL('./build/libfortranlib.dylib')

if __name__=="__main__":

    vec3 = pythontypes.Vec3()
    vec3.x1 = 1.0
    vec3.x2 = 2.0
    vec3.x3 = 3.0

    fortranlib.print_vec3.argtypes = [
	    POINTER(pythontypes.Vec3)
    ]
    fortranlib.print_vec3.restype = c_int
    fortranlib.print_vec3(vec3)


    string = pythontypes.Strings()
    string.string8 = b"abcdefgh"
    string.string1024 = b"abcdefghijklmnopqrstuvwxyz"

    fortranlib.print_strings.argtypes = [
        POINTER(pythontypes.Strings)
    ]
    fortranlib.print_strings.restype = c_int
    fortranlib.print_strings(string)


    arrays = pythontypes.Arrays()
    arrays.one_by_two = (c_float * 2)(1.0, 5.0)

    fortranlib.print_array_info.argtypes = [
        POINTER(pythontypes.Arrays)
    ]
    fortranlib.print_array_info.restype = c_int
    fortranlib.print_array_info(arrays)
