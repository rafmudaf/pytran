cmake_minimum_required(VERSION 3.6)
project(pytran VERSION 0.1 LANGUAGES Fortran)

if(CMAKE_SYSTEM_NAME MATCHES Darwin)
  set(CMAKE_MACOSX_RPATH 1)
endif()

if(CMAKE_Fortran_COMPILER_ID MATCHES GNU)
  set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -g")
  # set(CMAKE_Fortran_FLAGS "${CMAKE_Fortran_FLAGS} -fprofile-arcs -ftest-coverage")
endif()

# configure the newton-raphson module libraries
add_library(fortranlib
  SHARED
  ${CMAKE_CURRENT_LIST_DIR}/fortranlib.F90
  ${CMAKE_CURRENT_LIST_DIR}/fortran_types.F90
)
