#include <stdio.h>

void main()
{
    int num[] = {123,5,6,889,1};
    int i = 0;

    while(i <= 4)
    {
        // num points to address @ 0th element by default
	printf("\n%x\t%x", &num[i], num);
	printf("\n%d, %d, %d, %d", num[i], *(num + i), *(i + num), i[num]);
	i++;
	//compiler takes num and i, sums it and finds the value so all the above mean the same
    }
}
