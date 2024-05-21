def partition(A, left, right):
    low = left
    high = right
    mid = (low + high) // 2
    # 새 리스트에 왼쪽, 오른쪽, 중앙값 넣고 정렬해 중간값 찾기
    lista = []
    lista.append(A[low])
    lista.append(A[high])
    lista.append(A[mid])
    lista.sort()
    pivot = lista[1]
    print("pivot :", pivot)
    while low <= high:
        # 피벗값을 리스트 맨 왼쪽으로 이동시키기, 이후 계산은 동일하게 진행
        A[A.index(pivot)], A[left] = A[left], A[A.index(pivot)]
        while low <= right and A[low] <= pivot: 
            low += 1
        while high >= left and A[high] > pivot: 
            high -= 1
        if low < high:
            A[low], A[high] = A[high], A[low]
    A[left], A[high] = A[high], A[left]
    print(A)
    lista.clear()
    return high

def quick_sort(A,left,right):
    if left < right:
        mid = partition(A,left,right)
        quick_sort(A,left,mid-1)
        quick_sort(A,mid+1,right)
        
data = [5,3,8,4,9,1,6,2,7]
print("Oringinal : ", data)
quick_sort(data, 0, len(data)-1)
print("QuickSort :", data)