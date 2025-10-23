#include <stdio.h>
#include <ctype.h>
#include <string.h>

int main()
{
    char arr[50];
    int up = 0;
    int low = 0;
    int digits = 0;
    int symbols = 0;

    printf("Enter a string: ");
    scanf("%[^\n]s", &arr);

    for (int i = 0; i < strlen(arr); i++)
    {
        if (isupper(arr[i]))
        {
            up++;
        }
        else if (islower(arr[i]))
        {
            low++;
        }
        else if (isdigit(arr[i]))
        {
            digits++;
        }
        else if (!isalnum(arr[i]) || isspace(arr[i]))
        {
            symbols++;
        }
    }

    printf("Uppercase letters: %d\n", up);
    printf("Lowercase letters: %d\n", low);
    printf("Digits: %d\n", digits);
    printf("Symbols: %d", symbols);

    return 0;
}