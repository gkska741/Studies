import sys
sys.stdin = open("../추가문제/input.txt")



TC = int(input())

for tc in range(TC):
    N, K = map(int, input().split())
    test_case = [[]]
    for i in range(N+2):
        test_case[0].append(0)
    cnt = 0
    a = 0
    sample = [0]
    for i in range(K):
        sample.append(1)
    sample.append(0)

    for i in range(N):
        column = list(map(int, input().split()))
        column.append(0)
        column.insert(0, 0)
        test_case.append(column)

        for j in range(N-K+1):
            a += 1
            if column[j:j+K+2] == sample:
                cnt += 1
            else:
                pass

    last_column = []
    for i in range(N+2):
        last_column.append(0)
    test_case.append(last_column)

    for n in range(N+2):
        for i in range(N-K+1):
            temp = []
            for j in range(K+2):
                temp.append(test_case[i+j][n])

            a += 1
            if temp == sample:
                cnt += 1
            else:
                pass

    print(f'#{tc+1} {cnt}')









