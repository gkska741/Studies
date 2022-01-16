
# 순열 생성
# 하나씩 선택, 순서대로 나열
# 요소들을 중복하여 쓰면 안된다

arr = ['A', 'B', 'C']

perm = []
for first in arr:
    if first in perm: continue
    perm.append(first)

    for second in arr:
        if second  in perm: continue
        perm.append(second)

        for third in arr:
            if third in perm: continue
            perm.append(third)
            print(perm)

            perm.pop()
        perm.pop()
    perm.pop()
print()        
#-----------------------------------------------------------------------
N = len(arr)
perm = []
for i in range(N):
    if arr[i] in perm: continue
    perm.append(arr[i])

    for j in range(N):
        if arr[j] in perm: continue
        perm.append(arr[j])

        for k in range(N):
            if arr[k] in perm: continue
            perm.append(arr[k])

            print(perm)

            perm.pop()
        perm.pop()
    perm.pop()
print()

def f(k):
    if k == N:
        print(perm)
    else:
        for i in range(N):
            if arr[i] in perm: continue
            perm.append(arr[i])

            f(k+1)

            perm.pop()

f(0)
