#202311388 김민상
#Chapter 1
#문제 2_ 알고리즘 1.5 파이썬으로 작성
def gcd(a, b) :
    alist = []
    blist = []
    max = 1
    for i in range(1, a+1) :
        if a % i == 0 :
            alist.append(i)
    for i in range(1, b+1) :
        if b % i == 0 :
            blist.append(i)
    if a > b :
        for i in range(1, a) :
            if i in alist and i in blist :
                max = i
    else :
        for i in range(1, b) :
            if i in alist and i in blist :
                max = i

    print(f"{a}의 약수 = ", alist)
    print(f"{b}의 약수 = ", blist)
    print(f"{a}와 {b}의 최대 공약수 = {max}")

gcd(60,28)