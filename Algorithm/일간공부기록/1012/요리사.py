from itertools import combinations
input = open('input.txt').readline
TC = int(input())


def eval_value(comb):
    for i in range(len(comb)):
        value = 0
        tup = comb[i]
        two = list(combinations(tup, 2))
        for xy in two:
            value += board[xy[0]][xy[1]]
        comb[i] = value


for tc in range(1, TC+1):

    N = int(input())
    board = []
    visited = [0] * (N)

    for _ in range(N):
        Si = list(map(int, input().split()))
        board.append(Si)

    for i in range(1, N):
        for j in range(i):
            board[j][i] += board[i][j]
            board[i][j] = 0
    value = 0
    value_list = []
    min_value = 10**5

    comb = list(combinations(list(range(N)), N//2))
    length = len(comb)
    comb_left = comb[:length//2]
    comb_right = list(reversed(comb[length//2:]))


    eval_value(comb_left)
    eval_value(comb_right)
    
    
    min_result = 10**5
    for i in range(len(comb_left)):
        result = abs(comb_left[i] - comb_right[i])
        min_result = min(min_result, result)

    print(f'#{tc} {min_result}')

    


