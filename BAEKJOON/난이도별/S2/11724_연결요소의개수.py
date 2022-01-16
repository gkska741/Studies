import sys
sys.stdin = open('input.txt')

N, L = map(int, input().split())

board = [[] for _ in range( N+1 )]
visited = [0] * (N+1)

def dfs(s):
    visited[s] = 1
    for w in board[s]:
        if visited[w] == 0:
            dfs(w)

for i in range(L):
    s, e = map(int, input().split())
    board[s].append(e)
    board[e].append(s)

cnt = 0
for i in range(1, N+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)





