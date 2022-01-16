TC = int(input())


def spin(lst, N):
    answer = []
    for i in range(N):
        coloum = []
        temp = []
        for j in range(N - 1, -1, -1):
            temp.append(str(lst[j][i]))
        coloum.append(''.join(temp))

        temp = []
        for j in range(N - 1, -1, -1):
            temp.append(str(lst[N - i - 1][j]))
        coloum.append(''.join(temp))

        temp = []
        for j in range(N):
            temp.append(str(lst[j][N - i - 1]))
        coloum.append(''.join(temp))

        answer.append(' '.join(coloum))
    return answer


result = []
for i in range(TC):
    N = int(input())
    sample_input = []
    for j in range(N):
        coloum = list(map(int, input().split()))
        sample_input.append(coloum)
    answer = spin(sample_input, N)
    result.append(answer)

for i in range(len(result)):
    print(f'#{i + 1}')
    for j in range(len(result[i])):
        print(result[i][j])
