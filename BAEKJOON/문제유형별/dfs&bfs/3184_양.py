input = open('input.txt').readline
from collections import deque
C, R = map(int, input().split())
board = [list(input().strip()) for _ in range(C)]
visited = [[False] * R for _ in range(C)]
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def bfs(c, r):
    wolves = 0
    sheeps = 0

    if board[c][r] == 'v':
        wolves += 1
    elif board[c][r] == 'o':
        sheeps += 1
    Q = deque()
    Q.append((c, r))
    while Q:
        c, r = Q.pop()

        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]

            if 0 <= nc < C and 0 <= nr < R:
                if not visited[nc][nr]:
                    visited[nc][nr] = True
                    if board[nc][nr] == 'v':
                        wolves += 1; Q.append((nc, nr))
                    if board[nc][nr] == '.':
                        Q.append((nc, nr))
                    if board[nc][nr] == 'o':
                        sheeps += 1; Q.append((nc, nr))
    if sheeps > wolves:
        wolves = 0
    else:
        sheeps = 0

    return wolves, sheeps
                    

wolves = 0
sheeps = 0
for c in range(C):
    for r in range(R):
        if board[c][r] != '#' and not visited[c][r]:
            visited[c][r] = True
            w, s = bfs(c, r)
            wolves += w
            sheeps += s

print(sheeps, wolves)
