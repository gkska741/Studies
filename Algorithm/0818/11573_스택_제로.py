import sys
sys.stdin = open('stack_zero.txt')

TC = int(input())

for i in range(TC):
    N = int(input())
    sequence = list(map(int, input().split()))

    stack_temp = []
    for j in range(N):
        if sequence[j] != 0:
            stack_temp.append(sequence[j])
        else:
            stack_temp.pop(-1)
    total = 0
    for k in range(len(stack_temp)):
        total += stack_temp[k]
    print(f'#{i+1} {total}')
