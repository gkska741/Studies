input = open('input.txt').readline
from collections import deque

board = ['x'] * 100001
visited = [False] * 100001
N, K = map(int, input().split())
board[N] = 0
Q = deque()
Q.append(N)
while Q:
    for _ in range(len(Q)):
        now_loc = Q.popleft()
        if now_loc *2 < 100001:
            if board[now_loc*2] == 'x':
                board[now_loc * 2] = board[now_loc]
                Q.append(now_loc * 2)
        for i in [-1, 1]:
            if 0 <= now_loc + i < 100001:
                if board[now_loc + i] == 'x':
                    board[now_loc + i] = board[now_loc]+1
                    Q.append(now_loc + i)
        if board[K] != 'x':
            break

print(board[K])

