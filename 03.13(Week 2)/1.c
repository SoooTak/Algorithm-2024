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
    printf("%d와 %d의 최대공약수 : %d", a, b, max);
    printf("\n김민상\n");
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