#include <stdio.h>

void main()
{
    char name[] = "amigo";
    char *ptr;
    char *p;

    ptr = &name[0];
    p = name;

    while(*p != '\0')
    {
	printf("%c\t%c\n", *ptr, *p);
        p++;
        ptr++;
    }
}
