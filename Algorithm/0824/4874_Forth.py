import sys
sys.stdin = open('4874_input.txt')


TC = int(input())

for case_number in range(1, TC+1):
    error = 0
    infix = list(input().split())

    icp = {'+': 1, '*': 2, '-': 3, '/': 4}
    Stack = []
    infix.pop()
    for ch in infix:
        if ch in icp:
            try:
                num1 = int(Stack.pop(-1))
                num2 = int(Stack.pop(-1))
                if icp[ch] == 1:
                    Stack.append(num1 + num2)
                elif icp[ch] == 2:
                    Stack.append(num1 * num2)
                elif icp[ch] == 3:
                    Stack.append(num2 - num1)
                elif icp[ch] == 4:
                    Stack.append(num2 // num1)
            except:
                error = 1
        else:
            Stack.append(ch)

    if len(Stack) == 1 and error == 0:
        print(f'#{case_number} {Stack[0]}')

    elif error == 1 or len(Stack) >= 2:
        print(f'#{case_number} error')



