#202311388 김민상
#Chapter 1
#문제 25_합집합, 교집합, 차집합 구하는 함수 구현

def plus(list1, list2) :
    return set(list1) | set(list2)

def equal(list1, list2) :
    return set(list1) & set(list2)

def minus(list1, list2) :
    return set(list1) - set(list2)

A = [1,3,5,7,9]
B = [1,5,9,2,4,6]

result1 = plus(A, B)
result2 = equal(A, B)
result3 = minus(A, B)

print(f"합집합 : {result1}")
print(f"교집합 : {result2}")
print(f"차집합(A - B) : {result3}")