input = open('input.txt').readline


def go_up(c, r):
    c -= 1
    if c == 0:
        return (c, r, 'finished')
    if r == 99:
        while board[c][r-1] == 0:
            c -= 1
            if c == 0:
                return (c, r, 'finished')
        return (c, r, 'left')
    elif r == 0:
        while board[c][r+1] == 0:
            c -= 1
            if c == 0:
                return (c, r, 'finished')
        return (c, r, 'right')
    else:
        while board[c][r+1] == 0 and board[c][r-1] == 0:
            c -= 1
            if c == 0:
                return (c, r, 'finished')
        if board[c][r+1]:
            return (c, r, 'right')
        else:
            return (c, r, 'left')
    

def go_left(c, r):
    while board[c][r-1] == 1:
        r -= 1
        if r == 0:
            break
    return (c, r)

def go_right(c, r):
    while board[c][r+1] == 1:
        r += 1
        if r == 99:
            break
    return (c, r)

TC = 10
for _ in range(1, TC+1):
    case_number = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        if board[-1][i] == 2:
            break


    c = 99
    r = i
    while c > 0:
        c, r, direction = go_up(c, r)
        #print(c, r, direction)

        if direction == 'left':
            c, r = go_left(c, r)
            #print(c, r, 'up')
        elif direction == 'right':
            c, r = go_right(c, r)
            #print(c, r, 'up')

    print(f'#{case_number} {r}')


        

