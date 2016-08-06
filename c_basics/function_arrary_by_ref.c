#include <stdio.h>

void main()
{
    int i;
    int marks[] = {101, 102, 100};
    for (i = 0; i <= 2; i++){
	//printf("\n%d", i);
        display(&marks[i]);
    }
}

display(int *n)
{
    printf("\n%d", *n);
    show(&n);
}

show(int **x) //key to have to tell that its a pointer to a pointer. **
{
    printf("\n%d\n", **x);
}
