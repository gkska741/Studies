import sys
sys.stdin = open('input.txt', 'r')

arr = input()


# 일반적인 해법
for s in range(0, len(arr), 7):
    n = 0
    for i in range(7):
        if arr[s+i] == '1':
            n = n*2 + 1
        else:
            n = n*2

    print(n, end=' ')
print()

#BEAT oper.

for s in range(0, len(arr), 7):
    n = 0
    for i in range(7):
        if arr[s + i] == '1':
            n = n | (1<< (6-i))
    print(n, end=' ')