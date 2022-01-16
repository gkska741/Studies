import sys
sys.stdin = open('palindrome2.txt')


for TC in range(10):
    case_number = int(input())
    board = []
    for i in range(100):
        column = list(input())
        board.append(column)

    temp = 0
    for y in range(100):
        for x in range(99):
            max_length = 1
            for word_length in range(2, 101 - x):
                for index in range(word_length//2):
                    if board[y][x+index] == board[y][x+word_length-index-1]:
                        max_length = word_length
                    else:
                        max_length = 0
                        break
                if max_length > temp:
                    temp = max_length

    for x in range(100):
        for y in range(99):
            max_length = 1
            for word_length in range(2, 101 - y):
                for index in range(word_length//2):
                    if board[y+index][x] == board[y+word_length-index-1][x]:
                        max_length = word_length
                    else:
                        max_length = 0
                        break
                if max_length > temp:
                    temp = max_length

    print(f'#{case_number} {temp}')




















