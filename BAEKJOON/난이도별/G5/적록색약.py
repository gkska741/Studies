input = open('input.txt').readline

import sys
sys.setrecursionlimit(10**6)

dc = [0, -1, 1, 0]
dr = [1, 0, 0, -1]
def dfs(c, r, ch):
    visited[c][r] = 1
    for i in range(4):
        new_c = c + dc[i]
        new_r = r + dr[i]

        if 0 <= new_c < n and 0 <= new_r < n:
            if not visited[new_c][new_r] and board[new_c][new_r] == ch:
                dfs(new_c, new_r, ch)


n = int(input())
board = [list(input().strip()) for _ in range(n)]

Green = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 'G':
            Green.append((i, j))


visited = [[0] * n for _ in range(n)]
normal = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs(i, j, board[i][j])
            normal += 1
RG_odd = 0

for tup in Green:
    i, j = tup
    board[i][j] = 'R'

visited = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            dfs(i, j, board[i][j])
            RG_odd += 1


print(normal, RG_odd)