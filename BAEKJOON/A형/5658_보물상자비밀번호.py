input = open('input.txt').readline
        
def rotate(arr, N, last_index):
    last_element = arr[last_index]
    arr[last_index] = 0
    arr[last_index - N] = last_element
    first_index = last_index - N 
    last_index -= 1
    
    return first_index, last_index, arr


def calc(first_index, arr, k):
    result = []
    for m in range(1, 5):
        value = ''
        for idx in range(first_index + k*(m-1), first_index + k*m):
            value += str(arr[idx])
        result.append(int(value, 16))
    return result



TC = int(input())
for case_number in range(1, TC+1):
    N, K = map(int, input().split())
    arr = [0] * 7
    arr += list(input())
    last_index = N+6
    first_index = 7
    values = []
    for i in range(N//4):   

        value_list = calc(first_index, arr, N//4)
        first_index, last_index, arr = rotate(arr, N, last_index)
        
        
        
        
        values += value_list
    
    result = sorted(list(set(values)), reverse=True)
    print(f'#{case_number} {result[K-1]}')
        




