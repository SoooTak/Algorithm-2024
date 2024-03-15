#202311388 김민상
#Chapter 1
#문제 7_최대공약수 알고리즘 속도 비교

#time 모듈 이용해 속도 측정 결과 : 
# 유클리드 알고리즘이 제일 짧은 시간이 소요됨. 반복문 (for문)의 반복 횟수 및 개수가 속도에 영향을 미친 것으로 생각됨.

import time

#문제2
def gcd1(a, b) :
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

start1 = time.time()
gcd1(60, 28)
end1 = time.time()
print(f"문제2 : {end1 - start1:.10f} 초\n")


#문제3
def gcd2(a, b) :
    alist = []
    max = 1
    for i in range(1, a + 1):
        if a % i == 0:
            alist.append(i)
    for i in range(0, len(alist)-1) :
        if b % alist[i] == 0 :
            max = alist[i]

    print(f"{a}의 약수 = ", alist)
    print(f"{a}와 {b}의 최대 공약수 = {max}")

start2 = time.time()
gcd2(60, 28)
end2 = time.time()
print(f"문제3 : {end2 - start2:.10f} 초\n")


def gcd3(a, b) :
    while b != 0 :
        r = a % b
        a = b
        b = r
    return a

start3 = time.time()
print("60과 28의 최대 공약수 =", gcd3(60,28))
end3 = time.time()
print(f"문제3 : {end3 - start3:.10f} 초")
