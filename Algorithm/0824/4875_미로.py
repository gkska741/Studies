import sys
sys.stdin = open('4875_input.txt')


def dfs(sc, sr):
    global result
    board[sc][sr] = 1
    for i in range(4):
        new_c = sc + dc[i]
        new_r = sr + dr[i]

        if 0 <= new_c <= size-1 and 0 <= new_r <= size-1:
            if board[new_c][new_r] == 0:
                dfs(new_c, new_r)
            elif board[new_c][new_r] == 3:
                result = 1
                return




TC = int(input())

for case_number in range(1, TC+1):
    size = int(input())
    board = [list(map(int, input())) for _ in range(size)]

    for i in range(size):
        for j in range(size):
            if board[i][j] == 2:
                sc = i
                sr = j

    dc = [0, 0, 1, -1]
    dr = [1, -1, 0, 0]
    # 우 좌 하 상
    result = 0
    dfs(sc, sr)
    print(f'#{case_number} {result}')



