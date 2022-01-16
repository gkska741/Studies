TC = 10

def max_num(lst):
    max = 0
    for value in lst:
        if value >= max:
            max = value
        else:
            pass
    return max

def min_num(lst):
    min = lst[0]
    for value in lst:
        if value <= min:
            min = value
        else:
            pass
    return min

def max_num_index(lst):
    max = max_num(lst)
    for i in range(len(lst)):
        if lst[i] == max:
            break
        else:
            pass
    return i

def min_num_index(lst):
    min = min_num(lst)
    for i in range(len(lst)):
        if lst[i] == min:
            return i
        else:
            pass
    return i


def dumping(Dump, sequence):

    while Dump > 0:
        max_index = max_num_index(sequence)
        min_index = min_num_index(sequence)

        sequence[max_index] -= 1
        sequence[min_index] += 1

        ret = max_num(sequence) - min_num(sequence)
        if ret < 2:
            print('차이<2')
            return ret
        else:
            Dump -= 1

    return max_num(sequence) - min_num(sequence)


result = []
for i in range(TC):
    Dump = int(input())
    sequence = list(map(int, input().split()))

    answer = dumping(Dump, sequence)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')

