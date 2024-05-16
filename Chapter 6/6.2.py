def counting_sort(A) :
    output = [0] * len(A)
    count = [0] * MAX_VAL
    
    for i in A:
        count[i] += 1
    
    for i in range(MAX_VAL) :
        count[i] += count[i-1]
        
    for i in range(len(A)) :
        output[count[A[i]]-1] = A[i]
        count[A[i]] -= 1
        
    for i in range(len(A)) :
        A[i] = output[i]
    
MAX_VAL = 10
data = [1, 4, 1, 2, 7, 5, 2]
print("original : ", data)
counting_sort(data)
print("counting : ", data)
