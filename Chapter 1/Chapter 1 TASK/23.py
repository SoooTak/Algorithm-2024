#202311388 김민상
#Chapter 1
#문제 23_큐 이용 피보나치수열 출력

list = [0, 1]
temp = int(input("피보나치 수열의 출력할 항 개수 : "))
for i in range(2, temp) :
    list.append(list[i-1] + list[i-2])
print(list)