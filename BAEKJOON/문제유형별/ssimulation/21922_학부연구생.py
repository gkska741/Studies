input = open('input.txt').readline

from collections import deque
C, R = map(int, input().split()) 

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]
board = [list(map(int, input().split())) for _ in range(C)]

air = []
for c in range(C):
    for r in range(R):
        if board[c][r] == 9:
            air.append((c, r))

visited = [[0] * R for _ in range(C)]

def bfs(arr):
    seat = 0
    for (c, r) in arr:

                    




