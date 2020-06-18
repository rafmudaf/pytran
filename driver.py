
import numpy as np
from ctypes import CDLL, POINTER, c_int, c_float
import pythontypes

fortranlib = CDLL('./build/libfortranlib.dylib')

if __name__=="__main__":

    ###
    # These examples simply pass a data structure to the Fortran
    # library, and it reads from the data and prints info
    # to the console. The data flow is one-way: from Python
    # to Fortran. There is no returned value from Fortran.
    ###
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

    ###
    # This examples passes data into the Fortran library
    # and receive return values back through an INTENT(OUT)
    # variable in the subroutine signature.
    ###

    # Create the two input arguments
    v1 = pythontypes.Vec3()
    v1.x1 = 1.0
    v1.x2 = 2.0
    v1.x3 = 3.0

    v2 = pythontypes.Vec3()
    v2.x1 = 4.0
    v2.x2 = 5.0
    v2.x3 = 6.0

    # Create the object for the returned value, but
    # dont assign any values to it
    v_res = pythontypes.Vec3()

    fortranlib.add_vec3.argtypes = [
	    POINTER(pythontypes.Vec3),
	    POINTER(pythontypes.Vec3),
	    POINTER(pythontypes.Vec3)
    ]
    fortranlib.add_vec3.restype = c_int
    fortranlib.add_vec3(v1, v2, v_res)
    print(f"{v1} + {v2} = {v_res}")

