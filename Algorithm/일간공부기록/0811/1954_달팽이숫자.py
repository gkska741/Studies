TC = int(input())

def snail_number(lst):
    length = len(lst)
    size = len(lst) ** 2
    direction = [[0, 1], [1, 0], [0, -1], [-1, 0]] #우하좌상
    x = 0
    y = 0
    num = 2
    j = 0
    lst[x][y] = '1'
    while num <= size:
        temp_x = x + direction[j][0]
        temp_y = y + direction[j][1]
        if (temp_x in [-1, length]) or (temp_y in [-1, length]) or (lst[temp_x][temp_y] != 0):
            j = (j + 1) % 4
            x = x + direction[j][0]
            y = y + direction[j][1]
            lst[x][y] = str(num)
        else:
            x = x + direction[j][0]
            y = y + direction[j][1]
            lst[x][y] = str(num)
        num += 1

    string = ''
    for i in range(length):
        if i != length-1:
            string += ' '.join(lst[i]) + '\n'
        else:
            string += ' '.join(lst[i])
    return string


result = []
for i in range(TC):
    initial_list = []
    size = int(input())
    for i in range(size):
        initial_list.append(size*[0])
    answer = snail_number(initial_list)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1}')
    print(result[i])


