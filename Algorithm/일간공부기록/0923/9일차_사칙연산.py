import sys
sys.stdin = open('input.txt')

TC = 10

def calc(a, b, c):
    if c == '+':
        return a+b
    elif c == '*':
        return a*b
    elif c == '-':
        return a-b
    else:
        return a/b


for case_number in range(1, TC+1):
    V = int(input())
    value = [0] * (V+1)
    P = list(range(V+1))
    L = [0] * (V+1)
    R = [0] * (V+1)
    
    for i in range(1, V+1):
        node_info = list(input().split())
        if node_info[1] in ['+', '-', '*', '/']:
            value[i] = node_info[1]
            L[i] = int(node_info[2])
            R[i] = int(node_info[3])
        else:
            value[i] = int(node_info[1])
    for i in range(V, 0, -1):
        if value[i] in ['+', '-', '*', '/']:
            val = calc(value[L[i]], value[R[i]], value[i])
            value[i] = val
    
    print(f'#{case_number} {int(value[1])}')
    

        

    





