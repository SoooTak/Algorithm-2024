#202311388 김민상
#Chapter 1
#문제 8_최소공배수 알고리즘 작성

#두 수의 곱 = 최소공배수 x 최대공약수를 이용

def gcd(a, b) :
    temp = a * b
    print(f"{a}와 {b}의 최소공배수 = ", end=" ")
    if a < b :
        temp = a
        a = b
        b = temp
    while b != 0 :
        r = a % b
        a = b
        b = r
    print(f"{temp / a}")
    print(f"최대공약수 : {a}")
    
gcd(60, 28)