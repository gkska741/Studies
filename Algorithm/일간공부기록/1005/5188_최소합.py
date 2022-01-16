import sys
sys.stdin = open('input.txt', 'r')


def dfs(c, r):
    global value, result, abs_result

    value += board[c][r]

    if value >= abs_result:
        return
    
    if (c, r) == (N-1, N-1):
        if not result:
            result = value
        else:
            result = value
            abs_result = result
        return 

    else:
        for i in range(2):
            new_c = c + dc[i]
            new_r = r + dr[i]
            if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
                dfs(new_c, new_r)
                value -= board[new_c][new_r]

TC = int(input())
dc = [0, 1]
dr = [1, 0]
for case_number in range(1, TC+1):
    N = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))
    
    result = 0
    value = 0
    abs_result = 10**6
    dfs(0, 0)
    print(f'#{case_number} {result}')
