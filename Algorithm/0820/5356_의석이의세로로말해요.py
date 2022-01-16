import sys
sys.stdin = open('sayincolumn.txt')


TC = int(input())
for i in range(TC):
    board = []
    column = []
    for j in range(5):
        word = input()
        column.extend(word)
        board.append(column)
        column = []

    max_length = 0
    for j in range(5):
        length = len(board[j])
        if length >= max_length:
            max_length = length
        else:
            pass

    for j in range(5):
        while len(board[j]) < max_length:
            board[j].append('')

    answer = ''
    for k in range(max_length):
        for m in range(len(board)):
            answer += board[m][k]
    print(f'#{i+1} {answer}')










