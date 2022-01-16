import time
start = time.time()

input = open('input.txt').readline
TC = int(input())

def width():
    for i in range(9):
        if sum(board[i]) != 45:
            return False
    return True


def height():
    for i in range(9):
        value = 0
        for j in range(9):
            value += board[j][i]        
        if value != 45:
            return False
    return True


def miniboard():
    for m in range(3):
        for i in range(3):
            value = 0
            for j in range(3):
                for k in range(3):        
                    value += board[j+3*i][k+3*m]
            if value != 45:
                return False
    return True
            
    

            

for tc in range(1, TC +1):
    board = [list(map(int, input().split())) for _ in range(9)]

    if miniboard() and height() and width():
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')
# 3k ~ 3k+2 012 345 678

print(time.time() - start)
