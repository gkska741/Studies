import sys
sys.stdin = open('Iron.txt')

TC = int(input())

for i in range(TC):
    sample = list(input())
    case = []
    index = 0

    while index < len(sample):
        if sample[index] == '(' and sample[index+1] == ')':
            case.append('X')
            index += 2
        elif sample[index] == '(':
            case.append('(')
            index += 1
        else:
            case.append(')')
            index += 1

    j = 0
    total = 0
    temp_load = 0
    while j < len(case):
        if case[j] == 'X':
            total += temp_load

        elif case[j] == '(':
            temp_load += 1

        elif case[j] == ')':
            temp_load -= 1
            total += 1
        j += 1

    print(f'#{i+1} {total}')


    