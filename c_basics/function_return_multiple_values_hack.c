#include <stdio.h>

void main()
{
	int radius = 5;
	float area, perimeter;
	area_perimeter(radius, &area, &perimeter);
        printf("Area %f", area);
        printf("\nPerimeter %f\n", perimeter);

}

area_perimeter(int r, float *a, float *p)
{
	*a = 3.14 * r * r;
	*p = 2 * 3.14 * r;
}
