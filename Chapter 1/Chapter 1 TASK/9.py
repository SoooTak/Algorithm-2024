#202311388 김민상
#Chapter 1
#문제 9_이차방정식 근 구하기

import math

def equal (a, b, c) :
    if (b*b - 4*a*c) > 0 :
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2 * a
        x2 = (-b - math.sqrt(b**2 - 4*a*c)) / 2 * a
        print(f"x1 : {x1},   x2 : {x2}")

    elif (b**2 - 4*a*c) == 0 :
        x1 = (-b + math.sqrt(b**2 - 4*a*c)) / 2 * a
        print(f"중근, x = {x1}")

    else :
        print("허근을 가짐")
    
a = int(input("a 입력 : "))
b = int(input("b 입력 : "))
c = int(input("c 입력 : "))

equal(a,b,c)