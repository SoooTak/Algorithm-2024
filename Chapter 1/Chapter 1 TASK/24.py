#202311388 김민상
#Chapter 1
#문제 24_우선순위 큐 이용 숫자 정렬
import heapq

def sort_with_heapq(num):
    heapq.heapify(num)
    sorted_num = []
    while num:
        sorted_num.append(heapq.heappop(num))
    return sorted_num

list =  []
while True :
    temp = int(input("리스트 내용 입력 (그만 입력하려면 -1 입력) : "))
    if temp != -1 :
        list.append(temp)
    else :
        break
    
result = sort_with_heapq(list)
    
print(f"정렬된 결과: {result}")

