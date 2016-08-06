#include <stdio.h>

void main()
{
	float a = 7.99999;
	float *b, *c;
	b  = &a;
	c = b;
	printf("\n%u %u %u", &a, b, c);
	printf("\n%d %d %d %d\n", a, *(&a), *b, *c);
	printf("\n%f %f %f %f\n", a, *(&a), *b, *c);
}
