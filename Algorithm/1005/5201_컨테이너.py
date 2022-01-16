import sys
sys.stdin = open('input.txt')

TC = int(input())

for case_number in range(1, TC+1):
    N, M = map(int, input().split())
    Weight = sorted(list(map(int, input().split())), reverse=True)
    Tr = sorted(list(map(int, input().split())))

    print(Weight)
    print(Tr)

    val = 0
    for con in Weight:
        if Tr:
            if con <= Tr[-1]:
                Tr.pop()
                val += con
    print(f'#{case_number} {val}')