input = open('input.txt').readline
from collections import deque
TC = int(input())
dir = [(2, 1), (1, 2), (-1, 2), (2, -1), (-1, -2), (-2, -1), (1, -2), (-2, 1)]
for _ in range(TC):
    L = int(input())
    sc, sr = map(int, input().split())
    ec, er = map(int, input().split())

    board = [[0] * L for _ in range(L)]

    Q = deque()
    Q.append((sc, sr))

    while Q:
        for _ in range(len(Q)):
            c, r = Q.popleft()

            if (c, r) == (ec, er):
                break

            for dc, dr in dir:
                nc = c + dc
                nr = r + dr
                if 0 <= nc < L and 0 <= nr < L:
                    if board[nc][nr] == 0:
                        board[nc][nr] = board[c][r] + 1
                        Q.append((nc, nr))
        if board[ec][er]:
            break

    print(board[ec][er])


