import sys
sys.stdin = open("input.txt")


def where_first(sample):
    val = 0
    row = 0
    column = 99

    while val != 2:
        if sample[column][row] == 2:
            break
        else:
            row += 1
    dc = [0, 0, -1]  # 좌/우/상
    dr = [-1, 1, 0]
    k = 2
    while column > 0:
        if row != 0 and sample[column][row - 1] == 1 and k != 1:
            k = 0
        elif row != 99 and sample[column][row + 1] == 1 and k != 0:
            k = 1
        else:
            k = 2
        row += dr[k]
        column += dc[k]

    return row


TC = 10
result = []
for i in range(TC):
    sample_input = []
    n = int(input())
    for j in range(0, 100):
        sample_input.append(list(map(int, input().split())))
    answer = where_first(sample_input)
    print(f'#{i + 1} {answer}')
