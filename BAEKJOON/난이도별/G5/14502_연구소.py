input = open('input.txt').readline
import sys
from copy import deepcopy
from itertools import combinations
sys.setrecursionlimit(10**7)
C, R = map(int, input().split())

dc = [0, -1, 0, 1]
dr = [1, 0, -1, 0]

def bfs(n):
    visited = deepcopy(board)
    Q = []
    for two in initial_virus:
        Q.append(two)

    while Q:
        c, r = Q.pop()
        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]
            if 0 <= new_c <= C-1 and 0 <= new_r <= R-1:
                if board[new_c][new_r] == 0 and not visited[new_c][new_r]:
                    visited[new_c][new_r] = 2
                    n -= 1
                    Q.append((new_c, new_r))
    return n
            

board = [list(map(int, input().split())) for _ in range(C)]
wall_installable = []

initial_virus = []
for i in range(C):
    for j in range(R):
        if board[i][j] == 2:
            initial_virus.append((i, j))
        if board[i][j] == 0:
            wall_installable.append((i, j))
walls_installed = list(combinations(wall_installable, 3))

max_value = 0
num_of_zero = len(wall_installable)-3
for comb in walls_installed:

    for c, r in comb:
        board[c][r] = 1

    max_value = max(bfs(num_of_zero), max_value)
    
    
    for c, r in comb:
        board[c][r] = 0

print(max_value)
        


