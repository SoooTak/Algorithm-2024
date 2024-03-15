#202311388 김민상
#Chapter 1
#문제 5_ 유클리드 알고리즘 a가 작은 경우에도 작동하게 작성
def gcd(a, b) :
    if a < b :
        temp = a
        a = b
        b = temp
    print(f"gcd({a}, {b})")
    while b != 0 :
        r = a % b
        a = b
        b = r
        print(f"gcd({a}, {b})")
    return a

print("28과 60의 최대 공약수 =", gcd(28,60))