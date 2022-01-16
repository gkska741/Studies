def mergeSort(lst):

    if len(lst) == 1:
        return lst
    
    mid = len(lst) // 2
    left = mergeSort(lst[:mid])
    right = mergeSort(lst[mid:])

    result = []

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if left:
        result.extend(left)

    if right:
        result.extend(right)
    return result


arr = [7, 5, 3, 1, 2, 10, 4, 6, 9, 8]
N = len(arr)
tmp = [0]* N
def mergeSort(s, e):
    if s == e:
        return
    mid = (s + e) >> 1
    mergeSort(s, mid)
    mergeSort(mid + 1, e)

    # 정렬된 상태로 합친다.
    i, j, k = s, mid + 1, s
    while i <= mid and j <= e:
        if arr[i] < arr[j]:
            tmp[k] = arr[i]
            i, k = i + 1, k + 1
        else:
            tmp[k] = arr[j]
            j, k = j + 1, k + 1
    while i <= mid:
        tmp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= e:
        tmp[k] = arr[j]
        j, k = j + 1, k + 1
    for i in range(s, e + 1):
        arr[i] = tmp[i]
    print(arr[s: e + 1])

mergeSort(0, N - 1)
print(arr)

