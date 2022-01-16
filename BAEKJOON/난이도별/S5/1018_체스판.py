import sys
sys.stdin = open('input.txt')

C, R = map(int, input().split())

board = []

for i in range(C):
    column = list(input())
    board.append(column)

def White(Cs, Rs):
    cnt = 0
    for c in range(Cs, Cs+8):
        for r in range(Rs, Rs+8):
            if (r+c) % 2 == 0:
                if board[c][r] != 'W':
                    cnt += 1
            else:
                if board[c][r] != 'B':
                    cnt += 1
    return cnt

def Black(Cs, Rs):
    cnt = 0
    for c in range(Cs, Cs+8):
        for r in range(Rs, Rs+8):
            if (r+c) % 2 == 0:
                if board[c][r] != 'B':
                    cnt += 1
            else:
                if board[c][r] != 'W':
                    cnt += 1
    return cnt


if C == 8 and R == 8:
    white = White(0,0) 
    black = Black(0,0)
    min_value = min(white, black)
else:
    num_c = C-8+1
    num_r = R-8+1
    min_value = 10*6
    for cs in range(num_c):
        for rs in range(num_r):
            white = White(cs, rs)
            black = Black(cs, rs)
            min_value = min(min_value, white, black)

print(min_value)



