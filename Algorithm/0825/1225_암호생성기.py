import sys
sys.stdin = open('1225_input.txt')

TC = 10
for i in range(1, 11):
    case_number = int(input())
    q = list(map(int, input().split()))

    while 0 not in q:
        for x in range(1, 6):
            new_var = q.pop(0)-x
            if new_var <= 0:
                new_var = 0
                q.append(new_var)
                break
            else:
                q.append(new_var)
    q = list(map(str, q))
    answer = ' '.join(q)
    print(f'#{case_number} {answer}')



