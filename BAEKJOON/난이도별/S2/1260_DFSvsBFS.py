import sys
sys.stdin = open('input.txt')

def dfs(s):
    print(s, end=' ')
    visited[s] = 1
    for i in range(1, N+1):
        if board[s][i] == 1 and visited[i] == 0:
            dfs(i)

def bfs(s):
    Q = []
    Q.append(s)

    while Q:
        t = Q.pop(0)
        print(t, end=' ')
        if not visited[t]:
            visited[t] = 1
            
        for i in range(1, N+1):
            if board[t][i] and visited[i] == 0:
                Q.append(i)
                visited[i] = 1


N, M, V = map(int, input().split())

board = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    c, r = map(int, input().split())

    board[c][r] = 1
    board[r][c] = 1

visited = [0] * (N + 1)
dfs(V)
print()

visited = [0] * (N + 1)
bfs(V)


