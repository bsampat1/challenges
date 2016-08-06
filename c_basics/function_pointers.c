#include <stdio.h>

void main()
{
	int a = 10;
	int b = 20;
        printf("\n a=%d -- init", a);
	printf("\n b=%d -- init", b);
        swap_by_value(a, b);
        printf("\n a=%d -- after value", a);
	printf("\n b=%d -- after value", b);
	swap_by_reference(&a, &b);
        printf("\n a=%d -- after ref", a);
	printf("\n b=%d -- after ref\n", b);

}


swap_by_value(int x, int y)
{
	int tmp;
        tmp = x;
        x = y;
	y = tmp;
         printf("\n x=%d -- inside value", x);
	printf("\n y=%d -- inside value", y);      

}

swap_by_reference(int *x, int *y)
{
	int tmp;
        tmp = *x;
        *x = *y;
	*y = tmp;
}
