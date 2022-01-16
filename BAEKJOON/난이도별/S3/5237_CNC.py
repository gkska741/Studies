import sys

sys.stdin = open('input.txt')

case = int(input())

def dfs(s):
    visited[s] = 1
    for i in range(sites):
        if board[s][i] == 1 and visited[i] == 0:
            dfs(i)

for _ in range(case):
    
    seq = list(map(int,input().split()))
    sites = seq[0]
    lines = seq[1]

    board = [[0]*sites for _ in range(sites)]

    for i in range(1, lines+1):
        c, r = seq[2*i], seq[2*i + 1]
        board[c][r] = 1
        board[r][c] = 1

    visited = [0]*sites
    dfs(0)
    print(visited)
    if 0 in visited:
        print('Not connected.')
    else:
        print('Connected.')





