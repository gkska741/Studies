TC = int(input())

def numbers(lst, k):
    n = len(lst)
    cnt = 0
    for i in range(1 << n):
        temp = []
        for j in range(n):
            if i & (1 << j):
                temp.append(lst[j])
        total = 0
        for i in range(len(temp)):
            total += temp[i]

        if total == k:
            cnt += 1

    return cnt

result = []
for i in range(TC):
    N, K = map(int, input().split())
    sequence = list(map(int, input().split()))

    answer = numbers(sequence, K)
    result.append(answer)

for i in range(TC):
    print(f'#{i+1} {result[i]}')