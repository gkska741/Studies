TC = int(input())

for case_number in range(1, TC+1):
    N = int(input())

    board = [0] * N
    Need = list(map(int, input().split()))
    i = 1
    cnt = 0
    while board != Need:
        if board[i-1] != Need[i-1]:
            cnt += 1
            for j in range(1, N + 1):
                if j % i == 0:
                    if board[j-1] == 0:
                        board[j-1] = 1
                    else:
                        board[j-1] = 0
                else:
                    pass
        i = i + 1

    print(f'#{case_number} {cnt}')

