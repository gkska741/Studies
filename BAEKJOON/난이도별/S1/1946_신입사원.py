import sys
sys.stdin = open('input.txt')
"""
TC = int(input())
for case_number in range(1, TC+1):
    people_number = int(input())

    cnt = people_number

    people_score = []
    for i in range(people_number):
        person_score = list(map(int, input().split()))
        people_score.append(person_score)

        people_score.sort()

    for j in range(cnt-1):
        for i in range(j, cnt):
            if people_score[i][1] > people_score[j][1]:
                people_score[i] = [0, 0]
                cnt -= 1

    print(cnt)
"""   


# -----------------------------시간초과-------------------------------------
# TC = int(input())
# for case_number in range(1, TC+1):
#     people_number = int(input())

#     cnt = people_number

#     people_score = []
#     for i in range(people_number):
#         person_score = list(map(int, sys.stdin.readline().split()))
#         people_score.append(person_score)

#     people_score.sort()

#     for j in range(cnt-1):
#         for i in range(j, cnt):
#             if people_score[i][1] > people_score[j][1] and people_score[i] != [0, 0]:
#                 people_score[i] = [0, 0]
#                 cnt -= 1
#     print(cnt)

#     여기서 어떻게 줄일수 있을까요?

TC = int(input())
for case_number in range(1, TC+1):
    N = int(input())
    dp = []
    people_score = sorted([list(map(int, sys.stdin.readline().split())) for _ in range(N)])

    
    print(people_score)
    dp.append(people_score[0])
    cnt = 1
    
    for i in range(1, N): #들어갈 놈
        useless = False
        for j in range(N): #들어간 놈
            if people_score[i][1] > people_score[j][1]:
                useless = True
        
        if useless == True:
            pass
        else:
            dp.append(people_score[i])

    print(dp)
