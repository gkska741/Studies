import sys

sys.stdin = open("palindrome.txt")

TC = int(input())

for i in range(TC):
    N, M = map(int, input().split())
    board = []
    for j in range(N):
        board.append(input())
    palindrome = 0
    for j in range(N):
        for k in range(N-M+1):
            cnt = 0
            for p in range(M//2):
                if board[j][k+p] != board[j][M-p+k-1]:
                    break
                else:
                    cnt += 1
            if cnt == M//2:
                print(f'#{i+1} {board[j][k:M+k]}')
            else:
                pass

    for j in range(N):
        for k in range(N-M+1):
            cnt = 0
            for p in range(M//2):
                if board[k+p][j] != board[M-1-p+k][j]:
                    break
                else:
                    cnt += 1
            if cnt == M//2:
                string = ''
                for index in range(k, M+k):
                    string += board[index][j]
                print(f'#{i+1} {string}')
            else:
                pass



