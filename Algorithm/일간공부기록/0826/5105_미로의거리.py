import sys
sys.stdin = open('5105_input.txt')
from pprint import pprint
TC = int(input())

def bfs(sc, sr, deep):
    for i in range(4):
        global depth
        board[sc][sr] = 1
        new_c = sc + dc[i]
        new_r = sr + dr[i]
        if 0 <= new_c <= size-1 and 0 <= new_r <= size-1:
            if board[new_c][new_r] == 3:
                depth = deep
                return
            elif board[new_c][new_r] == 0:
                bfs(new_c, new_r, deep + 1)

for case_number in range(1, TC+1):
    size = int(input())
    board = [list(map(int, input())) for _ in range(size)]

    for y in range(size):
        for x in range(size):
            if board[y][x] == 2:
                sc = y
                sr = x

    dc = [0, 0, -1, 1] # 좌, 우, 상, 하
    dr = [-1, 1, 0, 0]
    depth = 0
    bfs(sc, sr, depth)
    print(f'#{case_number} {depth}')


