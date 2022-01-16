TC = int(input())


def sorting(sequence):
    i = len(sequence)
    while i > 1:
        for index in range(i-1):
            if sequence[index] > sequence[index+1]:
                temp = sequence[index]
                sequence[index] = sequence[index+1]
                sequence[index+1] = temp
            else:
                pass
        i = i-1
    sequence = list(map(str, sequence))
    return ' '.join(sequence)

result = []
for i in range(TC):
    N = int(input())
    sequence = list(map(int, input().split()))
    answer = sorting(sequence)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')