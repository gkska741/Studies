TC = 10

def sum_of_view(lst):
    total = 0
    for i in range(2, len(lst) - 2):
        temp = []

        for j in range(i - 2, i + 3):
            if lst[i] - lst[j] > 0:
                temp.append(int(lst[i] - lst[j]))
            else:
                continue

        if len(temp) == 4:
            min_num = temp[0]
            for i in range(len(temp)):
                if temp[i] <= min_num:
                    min_num = temp[i]
                else:
                    pass
            total += min_num
        else:
            pass
    return total


result = []

for i in range(TC):
    leng = int(input())
    arr = list(map(int, input().split()))
    tot = sum_of_view(arr)
    result.append(tot)

for i in range(len(result)):
    print(f'#{i + 1} {result[i]}')