TC = int(input())
result = []


def binary_search(sequence, key):
    arr = list(range(1, sequence[0]+1))
    lo = arr[0]
    hi = arr[-1]
    cnt = 1
    mid = ((lo + hi) // 2)
    while mid != key:
        mid = ((lo + hi) // 2)
        cnt += 1
        if arr[mid] > key:
            hi = mid
        else:
            lo = mid
    return cnt


for i in range(TC):
    sequence = list(map(int, input().split()))
    answerA = binary_search(sequence, sequence[1])
    answerB = binary_search(sequence, sequence[2])

    if answerA < answerB:
        result.append('A')
    elif answerA > answerB:
        result.append('B')
    else:
        result.append(0)

for i in range(len(result)):
    print(f'#{i + 1} {result[i]}')