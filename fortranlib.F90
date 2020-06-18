module fortranlib

    use iso_c_binding
    use fortran_types

    implicit none

    contains

    subroutine add_vec3(v1, v2, v_res) bind(c, name='add_vec3')
        type(Vec3), intent(in) :: v1, v2
        type(Vec3), intent(out) :: v_res

        v_res%x1 = v1%x1 + v2%x1
        v_res%x2 = v1%x2 + v2%x2
        v_res%x3 = v1%x3 + v2%x3

    end subroutine

    subroutine print_vec3(vector) bind(c, name='print_vec3')

        type(Vec3), intent(in) :: vector

        print *, "Vector components:"
        print *, vector%x1
        print *, vector%x2
        print *, vector%x3

    end subroutine

    subroutine print_strings(str) bind(c, name='print_strings')

        type(Strings), intent(in) :: str

        print *, "String8: ", str%string8
        print *, "String1024: ", str%string1024

    end subroutine

    subroutine print_array_info(array) bind(c, name='print_array_info')

        type(Arrays), intent(in) :: array

        print *, "Array info"
        print *, "  shape: ", shape(array%one_by_two)
        print *, "  values: ", array%one_by_two

    end subroutine

end module
