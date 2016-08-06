#include <stdio.h>
void main()
{
    int a[] = {10,20,30,40};
    int *pa [] = {a, a + 1, a + 2, a + 3};

    printf("\n Address of &pa[0]/pa: %x\t where address of &a[0]/a: %x\t is stored, where value of a[0]: %d\t is stored\n", pa, *pa, **pa); 
    printf("\n Address of &pa[0]/pa: %x\t where address of &a[0]/a: %x\t is stored, where value of a[0]: %d\t is stored\n", &pa[0], &a[0], a[0]); 
}
