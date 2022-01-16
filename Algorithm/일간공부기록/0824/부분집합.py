bits = [0] * 3

for i in range(2):
    bits[0] = i
    for j in range(2):
        bits[1] = j
        for k in range(2):
            bits[2] = k

def subset(k): #함수 호출의 depth
    if k == 3:
        print(bits)
    else:
        for i in range(2):
            bits[k] = i
            subset(k + 1)

#----------------------------------------------

arr = [1, 2, 3]
N = len(arr)
visit = [0] * N #요소의 선택 여부
order = [0] * N #실제 순열의 순서

def perm(k, N):
    if k == N:
        print(order)
    else:
        for i in range(N):
            if visit[i]: continue
            order[k] = arr[i]
            visit[i] = 1

            perm(k+1, N)
            visit[i] = 0

perm(0, N)
'''
for i in range(N):
    order[0] = arr[i]
    visit[i] = 1
    #--------------------------------------
    for j in range(N):
        if visit[j]: continue
        order[1] = arr[j]
        visit[j] = 1
        #------------------------------------
        for k in range(N):
            if visit[k]: continue
            order[2] = arr[k]
            visit[k] = 1
            print(order)
            visit[k] = 0

        visit[j] = 0

    visit[i] = 0
'''