import sys
sys.stdin = open('4886_input.txt')

TC = int(input())

for tc in range(TC):
    sample = input()
    stack = []
    target = ['(', ')', '{', '}', '[', ']']
    for i in range(len(sample)):
        if sample[i] in target:
            stack.append(sample[i])
        else:
            pass
    index = 0
    cnt = 0
    while len(stack) > 0 and len(stack) % 2 == 0:
        if index < len(stack)-1 and -3 < ord(stack[index]) - ord(stack[index+1]) < 0:
            for i in range(2):
                stack.pop(index)
            index = 0
            cnt = 0
            continue
        else:
            index += 1
            cnt += 1
            pass
        if cnt == len(stack):
            break

    if len(stack) == 0:
        print(f'#{tc + 1} {1}')
    else:
        print(f'#{tc + 1} {0}')










