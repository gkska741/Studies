import sys
sys.stdin = open('input.txt')

TC =int(input())

for case_number in range(1, TC+1):
    N, M = map(int, input().split())

    cnt = 0
    for i in range(N):
        if M & (1 << i):
            cnt += 1
    if cnt == N:
        print(f'#{case_number} ON')
    else:
        print(f'#{case_number} OFF')
