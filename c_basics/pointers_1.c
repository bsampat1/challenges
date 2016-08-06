#include <stdio.h>

void main()
{
    int i = 3;
    int *j; 
    j = &i; 
    int **k;
    k = &j;
    printf("\n Value of i =%d",**k);
    printf("\n Value of i = %d", *j);  
    printf("\n Address of i= %x", &i);
    printf("\n Value of i = %d\n", i); 
    printf("\n Address of j= %x", &j);
    printf("\n Address of i= %x\n", j);

}
