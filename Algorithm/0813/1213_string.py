import sys
sys.stdin = open('input_string.txt', encoding='UTF8')


TC = 10

for i in range(TC):
    case_number = int(input())
    word = input()
    sequence = input()
    cnt = 0

    for index in range(len(sequence)-len(word)+1):
        temp = 0
        for j in range(len(word)):
            if word[j] == sequence[index+j]:
                temp += 1
        if temp == len(word):
            cnt += 1
        else:
            pass

    print(f'#{case_number} {cnt}')





