TC = 10

result = []

def sum_x(lst):
    total = 0
    for i in range(100):
        total += lst[i]
    return total

result = []
for i in range(TC):
    N = int(input())

    test = []
    for i in range(100):
        column = list(map(int, input().split()))
        test.append(column)

    answer = 0
    maxval1 = 0
    for i in range(100):
        answer += test[i][i]

    maxval2 = 0
    for i in range(100):
        maxval2 += test[i][99-i]

    if maxval1 >= maxval2:
        answer = maxval1
    else:
        answer = maxval2

    for i in range(100):
        if sum_x(test[i]) >= answer:
            answer = sum_x(test[i])
        else:
            pass

    for i in range(100):
        total = 0
        for j in range(100):
            total += test[j][i]
        if total >= answer:
            answer = total
        else:
            pass
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')