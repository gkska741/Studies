input = open('input.txt').readline

dc = [0, 1, 0, -1]
dr = [1, 0, -1, 0]

TC = int(input())

for tc in range(10):
    size = int(input())
    board = [[0] * size for _ in range(size)]
    
    c = 0
    r = 0

    number = 1
    i = 0
    while number <= size ** 2:
        board[c][r] = number

        if 0 <= c + dc[i] <= size-1 and 0 <= r + dr[i] <= size-1 and board[c+dc[i]][r+dr[i]] == 0:
            c += dc[i]; r += dr[i]
        else:
            i = (i + 1) % 4
            c += dc[i]; r += dr[i]
        
        number += 1
    print(f'#{tc+1}')
    for i in range(len(board)):
        print(*board[i])

        