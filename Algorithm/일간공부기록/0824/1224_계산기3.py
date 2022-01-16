import sys
sys.stdin = open('1224_input.txt')

TC = 10

isp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 0, ')': 4}
icp = {'*': 2, '/': 2, '+': 1, '-': 1, '(': 3, ')': 4}

for case_number in range(1, TC+1):
    postfix = []
    Stack = []
    length = int(input())
    problem = input()

    for ch in problem:
        if ch in icp:
            if not Stack:
                Stack.append(ch)
            if ch == ')':
                while Stack[-1] != '(':
                    postfix.append(Stack.pop())
                Stack.pop()

            elif icp[ch] > isp[Stack[-1]]:
                Stack.append(ch)

            elif icp[ch] <= isp[Stack[-1]]:
                while isp[Stack[-1]] >= icp[ch]:
                    postfix.append(Stack.pop())
                Stack.append(ch)
        else:
            postfix.append(ch)

    result = []
    for ch in postfix:
        if ch in icp:
            num2 = int(result.pop())
            num1 = int(result.pop())
            if ch == '+':
                result.append(num1+num2)
            elif ch == '*':
                result.append(num1*num2)
            elif ch == '-':
                result.append(num1-num2)
            else:
                result.append(num1//num2)
        else:
            result.append(ch)

    print(f'#{case_number} {result[0]}')
