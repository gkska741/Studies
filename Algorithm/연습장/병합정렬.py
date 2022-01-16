arr = [4, 2, 5, 8, 1, 3, 6]

def merge_sort(m):
    if len(m) == 1:
        return m
    
    mid = len(m) //2

    left = merge_sort(m[:mid])
    right = merge_sort(m[mid:])

    return merge(left, right)


def merge(left, right):
    result = []

    while len(left) > 0 and len(right) >0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    
    if len(right) > 0:
        result.extend(right)
        
    if len(left) > 0:
        result.extend(left)
    
    return result

print(arr)
arr = merge_sort(arr)
print(arr)

