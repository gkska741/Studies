arr = [10, 8, 5, 3, 11, 6]

def BubbleSort(arr):
    L = len(arr) 
    for i in range(L-1, 0, -1):
        for j in range(0, i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    return arr

print(arr)
print(BubbleSort(arr))
