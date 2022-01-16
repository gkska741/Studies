import sys
from pprint import pprint
sys.stdin = open('input.txt')

TC = int(input())


def bfs(c, r):
    day_memo = [0]
    visited = [[0]*(R) for _ in range(C)]

    Q = [(c, r)]
    while Q:
        day_memo.append(len(Q) + day_memo[-1])       
        print(day_memo)

        temp = []
        while Q:
            point = Q.pop()
            c, r = point
            visited[c][r] = 1
            dv = categorize(c, r)
            for i in range(len(dv)):
                dc = dv[i][0]
                dr = dv[i][1]
                new_c = c + dc
                new_r = r + dr

                if 0 <= new_c <= C-1 and 0 <= new_r <= R-1:
                    if board[new_c][new_r] and not visited[new_c][new_r]:
                        if not (new_c, new_r) in temp:
                            temp.append((new_c, new_r))
        Q = temp
        print(Q)

def categorize(c, r): #[[dc, dr]]
    if board[c][r] == 1:
        dv = [[0, -1], [0, 1], [-1, 0], [1, 0]] 
        return dv
    
    elif board[c][r] == 2:
        dv = [[1, 0], [-1, 0]]
        return dv

    elif board[c][r] == 3:
        dv = [[0, 1], [0, -1]]
        return dv

    elif board[c][r] == 4:
        dv = [[-1, 0], [0, 1]]
        return dv
    elif board[c][r] == 5:
        dv = [[1, 0], [0, 1]]
        return dv
    elif board[c][r] == 6:
        dv = [[0, -1], [1, 0]]
        return dv
    else:
        dv = [[0, -1], [-1, 0]]
        return dv

for case_number in range(1, TC+1):
    board = []
    C, R, sc, sr, T = map(int, input().split())
    for i in range(C):
        column = list(map(int, input().split()))
        board.append(column)

    bfs(sc, sr)

    print()
