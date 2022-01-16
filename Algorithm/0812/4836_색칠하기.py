TC = int(input())
def paint_into_list(sequence):
    lengthx = sequence[2] - sequence[0] + 1
    lengthy = sequence[3] - sequence[1] + 1
    result = []
    for x in range(lengthx):
        for y in range(lengthy):
            result.append((sequence[0]+x, sequence[1]+y))
    return result
#sequence = (2 2 4 4 1)

def within(sample):
    red = []
    blue = []
    for i in range(len(sample)):
        if sample[i][-1] == 1:
            red = red + (paint_into_list(sample[i]))
        else:
            blue = blue + (paint_into_list(sample[i]))
    red = (set(red))
    blue = (set(blue))
    cnt = 0
    for comp in red:
        if comp in blue:
            cnt += 1
        else:
            pass
    return cnt





result = []
for i in range(TC):
    N = int(input())
    sample = []
    for i in range(N):
        paint = list(map(int, input().split()))
        sample.append(paint)
    answer = within(sample)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')
