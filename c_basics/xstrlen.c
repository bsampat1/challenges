#include <stdio.h>

void main()
{
    char str[] = "Hola Amigo!, Coma Estas.";
    printf("The length of str is %d\n", xstrlen(str));

}

int xstrlen(char *str)
{
    int len = 0;
    while (*str != '\0')
    {
	len++;
        str++;
    }
return (len);
}
