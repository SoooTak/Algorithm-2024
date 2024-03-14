/*
    프로그램 내용 : 유클리드 알고리즘을 이용한 최대공약수 구하기
    실습일 : 2024.03.13(수)
    실습자 : 김민상 (202311388)
*/
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <windows.h>    // VS Code Ctrl + F5로 실행시 cmd창이 바로 닫히는 현상으로 인해 system("pause"); 사용
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