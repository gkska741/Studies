TC = int(input())

def maxsum(sequence):
    temp = []
    for i in range(len(sequence)-1):
        temp.append(sequence[i]+sequence[i+1])
    max_num = 0
    for i in range(len(answer)):
        if answer[i] >= max_num:
            max_num = answer[i]
        else:
            pass
    return max_num


result = []
for i in range(TC):
    num = int(input())
    sequence = list(map(int, input().split()))
    answer = maxsum(sequence)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')
