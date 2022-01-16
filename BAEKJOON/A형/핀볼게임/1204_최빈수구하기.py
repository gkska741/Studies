input = open('input.txt').readline

TC = int(input())

for _ in range(TC):
    case_number = int(input())
    score_list = [0] * 101

    students_score = list(map(int, input().split()))
    max_cnt = 0
    while students_score:
        score = students_score.pop()
        score_list[score] += 1

        if score_list[score] > max_cnt:
            max_cnt = score_list[score]

    for i in range(100, -1, -1):
        if score_list[i] == max_cnt:
            break
    print(i)


