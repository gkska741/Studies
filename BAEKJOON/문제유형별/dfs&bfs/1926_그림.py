input = open('input.txt').readline
from collections import deque
dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def bfs(tup):
    Q = deque()
    Q.append(tup)  
    area = 1
    while Q:
        c, r = Q.pop()
        for i in range(4):
            nc = c + dc[i]
            nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R:
                if board[nc][nr] and not visited[nc][nr]:
                    visited[nc][nr] = 1
                    area += 1
                    Q.append((nc, nr))

    return area
                    
    


C, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(C)]
visited = [[0] * R for _ in range(C)]
num_of_area = 0
area = 0
for c in range(C):
    for r in range(R):
        if board[c][r]:
            if not visited[c][r]:
                visited[c][r] = 1
                sample_area = bfs((c, r))
                area = max(sample_area, area)
                num_of_area += 1

print(num_of_area)
print(area)

        
