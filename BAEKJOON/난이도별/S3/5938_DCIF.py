import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [[0]* ( N + 1 ) for _ in range(N+1) ]

def dfs(s):
    visited[s] = 1
    for i in range(1, N+1):
        if board[s][i] == 1 and visited[i] == 0:
            dfs(i)

for i in range(M):
    c, r = map(int, input().split())

    board[c][r] = 1
    board[r][c] = 1


visited = [0] * (N + 1)
res = 0

dfs(1)
for i in range(1, N+1):
    if visited[i] == 0:
        print(i)
        res += 1
if res == 0:
    print(0)

