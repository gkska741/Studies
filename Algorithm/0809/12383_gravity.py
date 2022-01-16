TC = int(input())


def gravity(sample):
    answer = []
    for i in range(len(sample)):
        cnt = 1
        for j in range(i+1, len(sample)):
            if sample[i] <= sample[j]:
                cnt += 1
        grav = len(sample)-i-cnt
        answer.append(grav)

    max_num = 0
    for i in range(len(answer)):
        if answer[i] >= max_num:
            max_num = answer[i]
        else:
            pass
    return max_num


result = []
for i in range(TC):
    N = int(input())
    sample = list(map(int, input().split()))
    answer = gravity(sample)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')