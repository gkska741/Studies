import sys
sys.stdin = open('input.txt')


def subtree(n):
    global cnt
    cnt += 1
    if not P[n]:
        return
    else:
        if L[n]:
            subtree(L[n])
        if R[n]:
            subtree(R[n])

TC = int(input())
for case_number in range(1, TC+1):
    E, N = map(int, input().split())
    
    P = [0] * (E+2)
    L = [0] * (E+2)
    R = [0] * (E+2)

    tree_info = list(map(int, input().split()))
    for i in range(E):
        P[tree_info[2*i]] = 1
        if L[tree_info[2*i]] == 0:
            L[tree_info[2*i]] = tree_info[2*i+1]
        else:
            R[tree_info[2*i]] = tree_info[2*i+1]
    cnt = 0
    subtree(N)
    print(f'#{case_number} {cnt}')





