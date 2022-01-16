import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
board = [[] for _ in range(N+1)]
for i in range(M):
    e, s = map(int, input().split())
    board[s].append(e)

visited = [0]*(N+1)



bfs()