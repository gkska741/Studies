input = open('input.txt').readline
from collections import deque

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def bfs(c, r, size):
    visited = [[0] * N for _ in range(N)]
    visited[c][r] = 1

    Q = deque()
    Q.append((c, r))
    distance = 0
    result = []
    while Q:

        temp = []
        distance += 1

        while Q:
            c, r = Q.popleft()

            for i in range(4):
                nc = c + dc[i]
                nr = r + dr[i]

                if 0 <= nc <= N-1 and 0 <= nr <= N-1:

                    if board[nc][nr] <= size and not visited[nc][nr]:
                        temp.append((nc, nr))
                        visited[nc][nr] = 1
                        if board[nc][nr] and board[nc][nr] < size:
                            result.append((nc, nr, distance))
        for x in temp:
            Q.append(x)
    return result     

def eat_fish(lst, size):
    global cnt

    pass
        
def find_fish(N, size):
    for i in range(N):
        for j in range(N):
            if board[i][j] and board[i][j] < size:
                fish_list.append((i, j))
    return fish_list






N = int(input().strip())
board = [list(map(int, input().strip().split())) for _ in range(N)]

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            c = i
            r = j

size = 2
cnt = 0
while True:

    fish_list = find_fish(N, size)
    
    if len(fish_list) < size:
        print(cnt)
        break

    eat_fish(fish_list, size) # fish_list를 받아서 size만큼 먹은 뒤 size+1
    break    
