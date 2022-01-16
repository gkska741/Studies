import sys
sys.stdin = open('input.txt')

def checknode(index, value):
    global max_value
    
    if value <= max_value:
        return
        
    if index == N:
        max_value = value

    for i in range(N):
        if visited[i]:
            visited[i] = 0
            checknode(index+1, value * board[index][i]/100)
            visited[i] = 1

TC = int(input())
for tc in range(1, TC +1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_value = 0
    visited = [1] * (N+1)

    checknode(0, 1)

    print('#{} {:.6f}'.format(tc, max_value*100))
    