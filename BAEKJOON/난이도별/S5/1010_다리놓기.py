import sys
sys.stdin = open('input.txt')

from pprint import pprint
TC = int(input())

for i in range(1, TC+1):
    N, M = map(int, input().split())

    board = [[0]*(M+1)]
    board.append(list(range(M+1)))
    for i in range(N-1):
        board.append([0]*(M+1))
    for i in range(1, N+1):
        board[i][i] = 1



    pprint(board)
