TC = int(input())


def info_max(lst, size):
    n = size
    maxval = [0, 0, 0]
    dx = [-1, 1, 0, 0]  #좌 우 상 하
    dy = [0, 0, -1, 1]
    for i in range(n):
        for j in range(n): #기준좌표

            total = 0

            for k in range(4): #+상하좌우
                x = i + dx[k]
                y = j + dy[k]
                if (x in [-1, n]) or (y in [-1, n]): #벗어날경우 제외
                    pass
                else:
                    total += lst[x][y] #total에 +
            print(total, i, j)
            if total >= maxval[0]:
                maxval = [total, i, j]

            else:
                pass
    return maxval


result = []
for i in range(TC):
    input_list = []
    size = int(input())
    for i in range(size):
        column = list(map(int, input().split()))
        input_list.append(column)

    answer = info_max(input_list, size)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i][1]} {result[i][2]} {result[i][0]}')