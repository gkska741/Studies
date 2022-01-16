import sys, itertools
sys.stdin = open('input.txt')

TC = int(input())

def perm(n, k):
    if k == n:
        result.append(tuple(arr))
    else:
        for i in range(k, n):
            arr[k], arr[i] = arr[i], arr[k]
            perm(n, k+1)
            arr[i], arr[k] = arr[k], arr[i]

for case_number in range(1, TC+1):
    board = []
    N = int(input())
    for _ in range(N):
        board.append(list(map(int, input().split())))

    arr = list(range(2, N+1))
    result = []
    perm(N-1, 0)
    
    
    res = 10**6
    for tup in result:
        val = 0
        val += board[0][tup[0]-1] 
        val += board[tup[-1]-1][0]
        for x in range(len(tup)-1):
            val += board[tup[x]-1][tup[x+1]-1]
        res = min(val, res)

    print(f'#{case_number} {res}')


#--------------------------------------------------#
