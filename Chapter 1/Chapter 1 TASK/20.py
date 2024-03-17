#202311388 김민상
#Chapter 1
#문제 20_리스트에 같은 항목이 있는지 비교

list1 = []
list2 = []
temp = 1
count1 = 0
count2 = 0
result = False
result_temp = []
while True :
    temp = int(input("리스트1 내용 입력 (그만 입력하려면 -1 입력) : "))
    if temp != -1 :
        list1.append(temp)
        count1 += 1
    else :
        break
temp = 1
while True :
    temp = int(input("리스트2 내용 입력 (그만 입력하려면 -1 입력) : "))
    if temp != -1 :
        list2.append(temp)
        count2 += 1
    else :
        break
    
if count1 < count2 :
    temp = count1
    count1 = count2
    count2 = temp

for i in range(count2) :
    for j in range(count1) :
        if list1[j] == list2[i] :
            result = True
            result_temp.append(list1[j])

if result :
    print(f"두 배열은 공통 요소가 있음 : {result_temp}")
else :
    print("두 배열은 공통 요소가 없음")
