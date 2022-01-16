TC = int(input())

def total(lst):
    value = 0
    for i in range(len(lst)):
        value += lst[i]
    return value

def num_of_portion(N, K):
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    n = 12
    cnt = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(lst[j])
        if (len(temp) == N) and (total(temp) == K):
            cnt += 1
        else:
            pass
    return cnt
result = []
for i in range(TC):
    NK = list(map(int, input().split()))
    N = NK[0]
    K = NK[1]

    if ((1+N)*N/2) > K:
        result.append(0)
    else:
        answer = num_of_portion(N, K)
        result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')