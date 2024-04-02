#202311388 김민상
#Chapter 2
#순환 알고리즘 - 팩토리얼
def factorial(n) :
    if n == 1 :
        return 1
    else :
        return n * factorial(n-1)

num = int(input("숫자 입력 : "))
print(f"{num}! = {factorial(num)}")