import sys

sys.stdin = open("input.txt")

TC = int(input())

lib = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']
for i in range(TC):
    count = [0] * 10
    index, numbers = input().split()
    case = input().split()

    for j in range(int(numbers)):
        for k in range(10):
            if case[j] == lib[k]:
                count[k] += 1
                break
            else:
                pass

    print(index)
    for m in range(10):
        print((lib[m] + ' ') * count[m], end='')
    print()





