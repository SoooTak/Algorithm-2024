#202311388 김민상
#Chapter 1
#문제 19_리스트 최댓값, 최솟값 반환

def arr(list) :
    max = list[0]
    min = list[0]
    for i in range(1,len(list)) :
        if max < list[i] :
            max = list[i]
        if min > list[i] :
            min = list[i]
    temp = (min, max)
    return temp

list = [2,1,3,4,6,5]
arrr = []
arrr = arr(list)
print(arrr)