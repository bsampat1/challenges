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
    char names[2][10] = {
			    "Javier",
                            "Messi"
		       };
    
    printf("Size of array %d\n", sizeof(names)); 
    mem_efficient_strings();
}

void mem_efficient_strings()
{
    char *names[] = {
                       "Javier",
                       "Messi"
                   };
    //names is a pointer to 2 dimensional array.
    //it stores base address of two character arrays Javier and Messi
    // names[0] -> [base add of Javier] == [location where j from Javier is stored]
    // names[1] -> [base add of Messi] == [location where m from Messi is stored]
    // http://stackoverflow.com/questions/37538/how-do-i-determine-the-size-of-my-array-in-c
    printf("Size of array %d\n", sizeof(*names)); 
}
