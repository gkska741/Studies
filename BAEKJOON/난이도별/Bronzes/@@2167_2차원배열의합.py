import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())

board = [[0] * (R+1)]
for i in range(C):
    board.append([0] + list(map(int, input().split())))
TC = int(input())

for _ in range(TC):
    i, j, x, y = map(int, input().split())
    val = 0
    for c in range(i, x+1):
        for r in range(j, y+1):
            val += board[c][r]
    print(val)

