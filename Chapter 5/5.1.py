#202311388 김민상
def merge_sort(A, left, right) :
    if left < right :
        mid = (left + right) // 2
        merge_sort(A, left, mid)
        merge_sort(A, mid + 1, right)
        merge(A, left, mid, right)

def merge(A, left, mid, right) :
    k = left
    i = left
    j = mid + 1
    while i <= mid and j <= right :
        if A[i] <= A[j] :
            sorted[k] = A[i]
            i, k = i + 1, k + 1
        else :
            sorted[k] = A[j]
            j, k = j+1, k+1
    
    if i > mid :
        sorted[k : k+right-j+1] = A[j : right + 1]
    else :
        sorted[k : k+mid - i+1] = A[i : mid + 1]
    
    A[left : right + 1] = sorted[left : right+1]

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
listA = [8, 1, 7, 3, 9, 2, 4, 5]
sorted = [0] * len(data)
print("Original : ", data)
merge_sort(data, 0, len(data) - 1)
print("MergeSort : ", data)
print()
print("Original : ", listA)
merge_sort(listA, 0, len(listA) - 1)
print("MergeSort : ", listA)