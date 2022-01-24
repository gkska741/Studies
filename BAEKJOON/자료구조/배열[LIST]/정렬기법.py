# 1. 선택정렬
# 최소값부터 맨 앞과 교환하는 방식

arr = [1, 5, 2, 3, 6, 9, 7]
def select(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

# 2. k번쨰로 작은 원소를 찾는 알고리즘(O(kn))

def selectK(arr, k):
    for i in range(0, k):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr[k-1]