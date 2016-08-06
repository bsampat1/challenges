#include <stdio.h>

void main()
{
    int i = 54;
    float a = 3.14;
    char *c,*d;
    c=&i;
    d=&a;
    printf("%d, %x", *c, c);
    printf("\n %d, %x", *d, d); // see if you can increment this pointer value and get the value@d

    //dumb hack
    float *aa;
    aa = d; //note that I did not do a *d here, else it would have tried to fetch the value@d, instead I'm storing the base address of a which is in d into aa

    printf("\n %f", *aa); // I was able to print out with a dumb hack. just remember, always use same types. i.e use an int pointer for an int variable etc
}
