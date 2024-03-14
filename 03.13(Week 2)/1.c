#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>
int gcd(int a,int b);
int main(void)
{
    int a, b, max;
    srand((unsigned)time(NULL));
    a = rand() % 101;
    b = rand() % 101;
    if (a < b)
    {
        int temp;
        temp = a;
        a = b;
        b = temp;
    }
    max = gcd(a,b);
    printf("%d¿Í %dÀÇ ÃÖ´ë °ø¾à¼ö : %d", a, b, max);
    printf("\n±è¹Î»ó\n");
    system("pause");
    return 0;
}
int gcd(int a, int b)
{
    while(b!=0)
    {
        int r = a % b;
        a = b;
        b = r;
    }
    return a;
}