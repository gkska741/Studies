input = open('input.txt').readline
from collections import deque
from pprint import pprint
TC = int(input())

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def BFS():
    Q = deque()
    Q.append((0, 0))

    while Q:
        c, r = Q.popleft()
        for i in range(4):
            new_c = c + dc[i]
            new_r = r + dr[i]
            if 0 <= new_c <= N-1 and 0 <= new_r <= N-1:
                if my_map[c][r] + board[new_c][new_r] < my_map[new_c][new_r]:
                    my_map[new_c][new_r] = my_map[c][r] + board[new_c][new_r]
                    Q.append((new_c, new_r))

for tc in range(1, TC+1):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    
    my_map = [[0xffffff] * N for _ in range(N)]
    my_map[0][0] = 0
    BFS()
    print(f'#{tc} {my_map[N-1][N-1]}')

