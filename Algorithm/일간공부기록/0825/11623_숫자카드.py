import sys
sys.stdin = open('11623_input.txt')

TC = int(input())

for case_number in range(1, TC+1):

    N = list(range(1, int(input())+1))
    L = len(N)
    Q = [0] * 1000000

    for i in range(len(N)):
        Q[i] = N[i]
    i = 0
    L = len(N)
    front = 0
    rear = L-1

    i = 1
    index = L-1
    while front != rear:
        if i % 2:
            Q[front] = 0
            front += 1

        else:
            rear += 1
            Q[rear] = Q[front]
            Q[front] = 0
            front += 1
            index += 1
        print(Q[:30])
        i += 1
    print(f'#{case_number} {Q[index]}')