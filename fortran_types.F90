module fortran_types

    use iso_c_binding
    
    implicit none

    type, bind(C) :: Vec3
    
        real(kind=c_float) :: x1
        real(kind=c_float) :: x2
        real(kind=c_float) :: x3
    
    end type
    
    type, bind(C) :: Strings
    
        character(KIND=c_char), dimension(8) :: string8
        character(KIND=c_char), dimension(1024) :: string1024
    
    end type

    type, bind(C) :: Arrays

        real(kind=c_float), dimension(1, 2) :: one_by_two

    end type
    
end module
    