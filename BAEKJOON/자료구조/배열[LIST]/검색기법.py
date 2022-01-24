
# 1. 순차검색
# O(n)
arr = [1, 2, 3, 4, 5, 6]
def sequentialSearch(arr, n, key):
    i = 0
    while i < n:
        if arr[i] == key:
            return i
        else:
            i += 1
    if i == n:
        return -1

# 2. 이진검색
# 정렬이 되어있으므로, 시간복잡도는 O(n)
# 자료의 추가,삭제,변경시 자료구조를 항상 정렬상태로 유지해야 함.
arr = [1, 3, 4, 6, 8, 11, 14, 17, 21, 32]
def binarySearch(arr, key):
    start = 0
    end = len(arr)

    while start <= end:
        mid = (start+end)//2

        if arr[mid] == key:
            return True
        
        elif arr[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return False

