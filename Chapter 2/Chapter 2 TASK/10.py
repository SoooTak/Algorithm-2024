#202311388 김민상
#Chapter 2
#문제 10

import random

def find_fake(coinlist) :
    A = []
    B = []
    C = []
    d = 2
    f = 2
    status = False
    status2 = False
    if (len(coinlist) % 3 == 1) :
        d = coinlist.pop()
        status = True
    if (len(coinlist) % 3 == 2) :
        d = coinlist.pop()
        f = coinlist.pop()
        status2 = True
    for i in range(0, len(coinlist), 3) :
        A.append(coinlist[i])
        B.append(coinlist[i+1])
        C.append(coinlist[i+2])
        
    print(A)
    print(B)
    print(C)
    
    if status == True :
        print(d)
    if status2 == True :
        print(d)
        print(f)
    
    a = sum(A)
    b = sum(B)
    c = sum(C)
    
    if a == b == c :
        pick = A.pop()
        if pick > d or pick > f:
            print("가짜 동전이 더 가벼움")
        else :
            print("가짜 동전이 더 무거움")
    else :
        if a == b :
            if a > c :
                print("가짜 동전이 더 가벼움")
            else :
                print("가짜 동전이 더 무거움")
        if b == c :
            if b > a :
                print("가짜 동전이 더 가벼움")
            else :
                print("가짜 동전이 더 무거움")
        if c == a :
            if c > b :
                print("가짜 동전이 더 가벼움")
            else :
                print("가짜 동전이 더 무거움")


coin = random.randint(3, 20)
coinlist = []

fake = random.randint(1, coin)

for i in range(1, coin) :
    if i != fake :
        coinlist.append(2)
    else :
        pick = random.choice([1,3])
        coinlist.append(pick)

print(coinlist)

find_fake(coinlist)
