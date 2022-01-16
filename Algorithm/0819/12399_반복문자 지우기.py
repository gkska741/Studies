import sys
sys.stdin = open('12399_input.txt')

TC = int(input())

for tc in range(TC):
    string = list(input())

    stack = [string[0]]
    index = 1

    while index < len(string):
        if len(stack) == 0:
            stack.append(string[index])
        elif string[index] == stack[-1]:
            stack.pop(-1)
        else:
            stack.append(string[index])

        index += 1
    print(f'#{tc+1} {len(stack)}')







