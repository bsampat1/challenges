#include <stdio.h>
//anything which changes == lvalue(compiler)
//cannot change base address of a, else it won't be able to track it.
//it can't save beginning of array, hence lvalue error

void main()
{
    int a[] = {1,2,3,4,5};
    int j = 0;

    while(j < 5)
    {
	printf("\n%d\t", *a);
	a++;
    }
}

/*
lvalue_error_pointer_array.c: In function ‘main’:
lvalue_error_pointer_array.c:14:3: error: lvalue required as increment operand
  a++;
   ^
*/
