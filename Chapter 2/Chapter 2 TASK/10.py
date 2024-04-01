#202311388 김민상
#Chapter 2
#문제 10

import random
coin = random.randint(3, 20)

coinlist = []

fake = random.randint(0, coin)

for i in range(1, coin) :
    if i != fake :
        coinlist.append(2)
    else :
        pick = random.choice([1,3])
        coinlist.append(pick)

print(coinlist)

def find_fake(coinlist) :
    A = []
    B = []
    C = []
    if (len(coinlist) % 3 == 1) :
        d = coinlist.pop()
    if (len(coinlist) % 3 == 2) :
        d = coinlist.pop()
        f = coinlist.pop()
    for i in range(0, len(coinlist), 3) :
        A.append(coinlist[i])
        B.append(coinlist[i+1])
        C.append(coinlist[i+2])
    print(A)
    print(B)
    print(C)
    print(d)
    print(f)
find_fake(coinlist)
    