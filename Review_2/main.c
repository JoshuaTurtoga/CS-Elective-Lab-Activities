#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void reverseString(char *str)
{
    if (str == NULL || *str == '\0')
    {
        return;
    }

    char *start = str;
    char *end = str + strlen(str) - 1;

    while (start < end)
    {
        char temp = *start;
        *start = *end;
        *end = temp;

        start++;
        end--;
    }
}

int main()
{
    char myString[50];

    printf("\n=============================\n");
    printf("Enter a string: ");
    fgets(myString, sizeof(myString), stdin);

    printf("=============================");
    printf("\n\n");
    printf("Output:");
    printf("\n=============================\n");
    printf("Original String: \n%s", myString);
    reverseString(myString);
    printf("-----------------------------\n");
    printf("Reversed String: %s", myString);

    return 0;
}