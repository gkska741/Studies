TC = int(input())

def minmax(sequence):
    max = 0
    min = 1000000
    for i in range(len(sequence)):
        if sequence[i] >= max:
            max = sequence[i]
        else:
            pass
    for i in range(len(sequence)):
        if sequence[i] <= min:
            min = sequence[i]
        else:
            pass

    return max-min


result = []
for i in range(TC):
    N = int(input())
    sequence = list(map(int, input().split()))
    answer = minmax(sequence)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')