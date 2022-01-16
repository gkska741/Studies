import sys
sys.stdin = open('input.txt')
from pprint import pprint


N, M = map(int, input().split())
board= [[] for _ in range(N+1)]

for _ in range(M):
    old, young = map(int, input().split())
    board[old].append(young)

pprint(board)
def is_a_older_than_b(a0, a, b):
    visited[a] = 1
    if b in board[a]:
        return True    

    for i in range(1, N+1):
        if i in board[a] and not visited[i]:
            return is_a_older_than_b(a0, i, b)

Q = int(input())

for i in range(Q):
    visited = [0] * (N+1)
    a, b = map(int, input().split())
    a0 = a
    if is_a_older_than_b(a0, a,  b):
        print(a0, end=' ')
    else:
        b0 = b
        visited = [0] * (N+1)
        if is_a_older_than_b(b0, b, a):
            print(b0, end= ' ')
        else:
            print('gg', end=' ')
    
