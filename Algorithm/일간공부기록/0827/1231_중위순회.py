import sys; sys.stdin = open('1231_input.txt')



def inorder2(v):
    if v == 0: return

    inorder2(L[v])
    print(S[v], end='')
    inorder2(R[v])

for case_number in range(1, 11):
    V = int(input())

    L = [0] * (V + 1)
    R = [0] * (V + 1)
    P = [0] * (V + 1)
    S = [0] * (V + 1)

    for v in range(1, V + 1):
        info = list(input().split())
        S[v] = info[1]

        p = int(info[0])
        if len(info) == 4:
            lc = int(info[2])
            rc = int(info[3])

            L[p] = lc
            R[p] = rc
            P[lc] = p
            P[rc] = p

        if len(info) == 3:
            lc = int(info[2])
            L[p] = lc
            P[lc] = p
    print(f'#{case_number} ', end='')
    inorder2(1)
    print()

"""
V, E = map(int, input().split())
arr = list(map(int, input().split()))

L = [0] * (V + 1)
R = [0] * (V + 1)
P = [0] * (V + 1)
# E = V - 1
for i in range(0, E * 2, 2):
    p, c = arr[i], arr[i + 1]
    if L[p] == 0:
        L[p] = c
    else:
        R[p] = c
    P[c] = p

def inorder(v):
    if v == 0: return

    inorder(L[v])
    print(v, end=' ')
    inorder(R[v])
inorder(1)
"""