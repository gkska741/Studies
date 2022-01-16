import sys
sys.stdin = open('input.txt')

TC = int(input())

for case_number in range(1, TC+1):
    N = int(input())
    answer = 1
    board = [list(map(int, input().split())) for _ in range(N)]
    board.sort(key=lambda x: x[1], reverse=True)

    abs_end = board.pop()[1]
    while board:
        s, e = board.pop()

        if abs_end <= s:
            abs_end = e
            answer += 1

    print(f'#{case_number} {answer}')

