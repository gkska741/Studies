
Arr = [1, 2, 3, 4, 5]

def QuickSort(A, l, r):
    if l < r:
        s = partition_Lomuto(A, l, r)
        QuickSort(A, l, s-1)
        QuickSort(A, s+1, r)
    

def partition_Hoare(A, l, r):
    p = A[l]
    i = l+1
    j = r

    while i <= j:
        while (i <= j and A[i] <= p ): i += 1
        while (i <= j and A[i] >= p ): j -= 1

        if i <= j:
            A[i], A[j] = A[j], A[i]

    A[l], A[j] = A[j], A[l]
    return j 

def partition_Lomuto(A, l, r):
    x = A[r]
    i = l-1
    for j in range(l, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[r] = A[r], A[i+1]

    return i+1

print(Arr)
QuickSort(Arr, 0, len(Arr)-1)
print(Arr)
    

