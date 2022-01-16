input = open('input.txt').readline
from collections import deque
TC = int(input())


dc = [0, 0, -1, 1]
dr = [-1, 1, 0, 0]

def bfs(c1, r1):
    Q = deque()
    Q.append((c1, r1))

    while Q:
        c, r = Q.popleft()
        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]

            if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
                if visited[new_c][new_r] > board[new_c][new_r] + visited[c][r]:
                    visited[new_c][new_r] = board[new_c][new_r] + visited[c][r]
                    Q.append((new_c, new_r))
    
    return


    

for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    visited = [[0xfffff] * N for _ in range(N)]
    visited[0][0] = 0
    c = 0
    r = 0

    bfs(c, r)
    print(f'{tc} {visited[N-1][N-1]}')
