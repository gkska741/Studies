import sys
sys.stdin = open('1226_input.txt')
from pprint import pprint

def bfs(Q):
    global res
    while Q:
        temp = []
        while Q:
            y, x = Q.pop(0)
            visit.append((y, x))

            if board[y][x] == 3:
                res = 1
                return

            for i in range(4):
                new_y, new_x = y + dc[i], x + dr[i]

                if board[new_y][new_x] in [0, 3] and not (new_y, new_x) in visit:
                    temp.append((new_y, new_x))

            while temp:
                Q.append(temp.pop(0))

dc = [0, 0, -1, 1] # 좌, 우, 상, 하
dr = [-1, 1, 0, 0]

for _ in range(10):
    test_number = int(input())
    board = [list(map(int, input())) for _ in range(16)]
    visit = []
    Q = [(1, 1)]

    res = 0
    bfs(Q)
    print(f'#{test_number} {res}')
