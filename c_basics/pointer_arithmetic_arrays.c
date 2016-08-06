#include <stdio.h>

void main()
{
    int num[] = {11,22,33,44,15};
    int i = 0, *j;
    
    j = &num[0];
    
    while(i<=4)
    {
        printf("\naddress=%x\t", &num[i]);
        printf("element=%d", *j);
	i++;
	j++; //incrementing pointer of type int, goes to point to next int
    }
}
