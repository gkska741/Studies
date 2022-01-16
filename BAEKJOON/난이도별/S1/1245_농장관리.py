import sys
sys.stdin = open('input.txt')
from pprint import pprint

N, M = map(int, input().split())
dy = [0, 0, -1, 1, -1, -1, 1, 1] 
dx = [1, -1, 0, 0, -1, 1, -1, 1]
# 우 좌 상 하 좌상 우상 좌하 우하

board = [[0]*(M+1)]
for i in range(N):
    column = [0] + list(map(int, input().split()))
    board.append(column)


searched = [[0] * (M+1) for _ in range(N+1)]
sy = 1
sx = 1

cnt = 0

def dfs(sy, sx):
    print(f'dfs({sy}, {sx})')
    print(f'cnt = {cnt}')
    searched[sy][sx] = 1
    now_height = board[sy][sx]
    for i in range(8):
        new_y = sy + dy[i]
        new_x = sx + dx[i]
        if 1 <= new_y <= N and 1 <= new_x <= M:
            if board[new_y][new_x] > now_height:
                if not searched[new_y][new_x]:
                    now_height = board[new_y][new_x]
                    dfs(new_y, new_x)
                else:
                    searched[new_y][new_x] = 1
    

for y in range(1, N+1):
    for x in range(1, M+1):
        if not searched[y][x]:
            cnt += 1
            dfs(y, x)
