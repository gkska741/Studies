import sys
sys.stdin = open('1223_input.txt')

for case_number in range(1, 11):
    length = int(input())

    infix = input()
    postfix = []
    S = []
    icp = {'*': 2, '+': 1}

    for ch in infix:
        if ch in icp:
            if S:
                while S and icp[ch] <= icp[S[-1]]:
                    postfix.append(S.pop())
                S.append(ch)
            else:
                S.append(ch)
        else:
            postfix.append(ch)

    while S:
        postfix.append(S.pop())

    Stack = []
    for ch in postfix:
        if ch in icp:
            if icp[ch] == 2:
                num1 = int(Stack.pop(-1))
                num2 = int(Stack.pop(-1))
                Stack.append(num1*num2)
            else:
                num1 = int(Stack.pop(-1))
                num2 = int(Stack.pop(-1))
                Stack.append(num1+num2)
        else:
            Stack.append(ch)
    print(f'#{case_number} {Stack[0]}')
