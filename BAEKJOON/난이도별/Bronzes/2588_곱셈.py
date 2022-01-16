import sys
sys.stdin = open('input.txt')

A = int(input())
B = reversed(input())

board = []
for ch in B:
    val = A * int(ch)
    board.append(val)
    print(val)

res = 0
for i in range(3):
    res += board[i]*10**i

print(res)