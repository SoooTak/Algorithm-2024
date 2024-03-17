#202311388 김민상
#Chapter 1
#문제 26_진부분집합 구하는 함수 구현

def real(list1, list2) :
    return set(list1) < set(list2)

A = [1,3,5]
B = [1,3,5,7,9]
C = [2,4,6,8]
D = [1,3,6]

print(f"{A}는 {B}의 진부분집합이다 : {real(A, B)}")
print(f"{D}는 {B}의 진부분집합이다 : {real(D, B)}")