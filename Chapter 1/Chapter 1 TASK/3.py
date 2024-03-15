#202311388 김민상
#Chapter 1
#문제 3_ 알고리즘 1.6 파이썬으로 작성
def gcd(a, b) :
    alist = []
    max = 1
    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)
    for i in range(0, len(alist)) :
        if b % alist[i] == 0 :
            max = alist[i]

    print(f"{a}의 약수 = ", alist)
    print(f"{a}와 {b}의 최대 공약수 = {max}")

gcd(60, 28)