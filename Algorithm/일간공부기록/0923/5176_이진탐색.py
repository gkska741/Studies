import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10**6)

def tree(s):
    global cnt
    if L[s]:
        tree(L[s])
    Value[s] = cnt
    cnt += 1
    if R[s]:
        tree(R[s])
    
    
    
    pass

TC = int(input())
for case_number in range(1, TC+1):
    N = int(input())

    P = list(range(N+1))
    L = [0] * (N+1)
    R = [0] * (N+1)
    Value = [0] * (N+1)
    cnt = 2
    i = 1
    while cnt <= N:
        if not L[i]:
            L[i] = cnt
            cnt += 1
        elif not R[i]:
            R[i] = cnt
            cnt += 1
        else:
            i += 1
    cnt = 1
    tree(1)
    print(f'#{case_number} {Value[1]} {Value[N//2]}')



    
