input = open('input.txt').readline
from collections import deque
TC = int(input())

def find_set(x):
    if x != relation[x]:
        relation[x] = find_set(relation[x])
    return relation[x]

for tc in range(1, 1 + TC):
    N = int(input())

    X = [0] + list(map(int, input().split()))
    Y = [0] + list(map(int, input().split()))
    E = float(input())
    Q = []
    for j in range(1, N+1):
        for i in range(1, j+1):
            if i != j: 
                xi = X[i]; yi = Y[i]
                xj = X[j]; yj = Y[j]
                value = ((xj-xi)**2 + (yj-yi)**2)* E
                Q.append((i, j, value))
    Q.sort(key= lambda x: x[2], reverse=True)
    cnt = N-1
    result = 0
    relation = list(range(N+1))
    
    while cnt:
        i, j, value = Q.pop()
        a = find_set(i)
        b = find_set(j)
        if a == b: continue
        relation[b] = a
        result += value
        cnt -= 1
    print(f'#{tc} {round(result)}')


        


        


                



