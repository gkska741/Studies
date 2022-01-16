import sys

sys.stdin = open("input.txt")

TC = int(input())

lib = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for i in range(TC):
    index, numbers = input().split()
    case = input().split()
    answer = ''
    for j in range(10):
        for k in range(len(case)):
            if lib[j] == case[k]:
                answer += lib[j] + ' '
            else:
                pass
    answer = answer.strip()
    print(index)
    print(answer)




