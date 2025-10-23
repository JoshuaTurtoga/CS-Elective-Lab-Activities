#include <stdio.h>

int main()
{
    float carA, carB;
    float distance;

    printf("Enter distance in km: ");
    scanf("%f", &distance);
    printf("Enter fuel for Car A in L: ");
    scanf("%f", &carA);
    printf("Enter fuel for Car B in L: ");
    scanf("%f", &carB);

    float efficiencyA = distance / carA;
    float efficiencyB = distance / carB;

    float percent_diff;

    if (efficiencyA > efficiencyB)
    {
        percent_diff = (((efficiencyA - efficiencyB) / efficiencyB) * 100);
        printf("Car A is more efficient by %.2f%%", percent_diff);
    }
    else if (efficiencyB > efficiencyA)
    {
        percent_diff = (((efficiencyB - efficiencyA) / efficiencyA) * 100);
        printf("Car B is more efficient by %.2f%%", percent_diff);
    }
    else
    {
        printf("Both cars have the same efficiency");
    }
}