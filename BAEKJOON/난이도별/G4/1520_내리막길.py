from pprint import pprint
'''input
4 5
50 45 37 32 30
35 50 40 20 25
30 30 25 17 28
27 24 22 15 10
'''
import sys
sys.setrecursionlimit(10**6)
input = open('input.txt').readline
C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

cnt = 0
def dfs(c, r):
    global cnt
    if (c, r) == (C-1, R-1):
        return 1
    
    if visited[c][r] != -1:
        return visited[c][r]
    
    visited[c][r] = 0

    for i in range(4):
        new_c = c + dc[i]
        new_r = r + dr[i]

        if 0 <= new_c <= C-1 and 0 <= new_r <= R-1:
            if board[new_c][new_r] < board[c][r]:
                visited[c][r] += dfs(new_c, new_r)
    return visited[c][r]

visited = [[-1] * R for _ in range(C)]

print(dfs(0,0))
pprint(visited)




    




