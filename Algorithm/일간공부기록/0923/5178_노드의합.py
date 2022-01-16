import sys
sys.stdin = open('input.txt')

TC = int(input())


for case_number in range(1, TC+1):
    V, LV, M = map(int, input().split())
    Value = [0] * (V+1)
    for _ in range(LV):
        index, val = map(int, input().split())
        Value[index] = val

    P = list(range(V+1))
    L = [0] * (V+1)
    R = [0] * (V+1)

    for i in range(1, V+1):
        if 2*i <= V:
            L[i] = 2*i
        if 2*i+1 <= V:
            R[i] = 2*i + 1

    for i in range(V, 0, -1):
        if L[i] == 0 and R[i] == 0:
            pass
        else:
            Value[i] = Value[R[i]] + Value[L[i]]
    print(f'#{case_number} {Value[M]}')