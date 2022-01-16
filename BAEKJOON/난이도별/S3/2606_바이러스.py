import sys
sys.stdin = open('input.txt')
from pprint import pprint

N = int(input())
lines = int(input())

board = [[0] * (N+1) for _ in range(N+1)]
for i in  range(lines):
    c, r = map(int, input().split())
    board[c][r] = 1
    board[r][c] = 1

visited  = [0] * (N+1)
visited[1] = 1

def dfs(s):

    visited[s] = 1
    for i in range(1, N+1):
        if board[s][i] == 1 and visited[i] == 0:
            dfs(i)

dfs(1)
print(visited.count(1)-1)


