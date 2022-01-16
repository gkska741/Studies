import sys
sys.stdin = open('input.txt')

def isEmpty():
    return hsize == 0

def push(item):
    global hsize
    hsize += 1
    H[hsize] = item
    c = hsize; p = c // 2
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
        else:
            break
        c = p
        p = c // 2


TC = int(input())

for case_number in range(1, TC+1):
    V = int(input())
    H = [0] * (V+1)
    hsize = 0
    data = list(map(int, input().split()))
    for val in data:
        push(val)
    
    res = 0
    while V:
        V = V//2
        res += H[V]
    
    print(f'#{case_number} {res}')

    
