import sys
sys.stdin = open('5097_input.txt')

TC = int(input())

for case_number in range(1, TC+1):
    N, M = map(int, input().split())

    Q = [0] * 10000
    number_list = list(map(int, input().split()))
    for i in range(len(number_list)):
        Q[i] = number_list[i]

    front = 0
    rear = N-1

    for i in range(M):
        rear += 1
        Q[rear] = Q[front]
        Q[front] = 0
        front += 1

    print(f'#{case_number} {Q[front]}')