#202311388 김민상
#Chapter 1
#문제 4_ 유클리드 알고리즘 중간과정 보이게 작성
def gcd(a, b) :
    print(f"gcd({a}, {b})")
    while b != 0 :
        r = a % b
        a = b
        b = r
        print(f"gcd({a}, {b})")
    return a

print("60과 28의 최대 공약수 =", gcd(60,28))