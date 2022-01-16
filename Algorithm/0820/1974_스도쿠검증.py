TC = int(input())


def sdoku_function(sample):
    for k in [0, 3, 6]:
        temp = []
        for i in range(3):
            for j in range(3):
                temp.append(sample[i][j + k])
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
        else:
            pass
    return 1


def is_sdoku(sample):
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sample[i][j])
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
        else:
            pass

    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(sample[j][i])
        if sorted(temp) != [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            return 0
        else:
            pass

    list1 = [sample[0], sample[1], sample[2]]
    list2 = [sample[3], sample[4], sample[5]]
    list3 = [sample[6], sample[7], sample[8]]

    l1 = sdoku_function(list1)
    l2 = sdoku_function(list2)
    l3 = sdoku_function(list3)

    if 0 in [l1, l2, l3]:
        return 0
    else:
        return 1


result = []
for i in range(TC):

    sdoku = []
    for j in range(9):
        line = list(map(int, input().split()))
        sdoku.append(line)
    answer = is_sdoku(sdoku)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i + 1} {result[i]}')
