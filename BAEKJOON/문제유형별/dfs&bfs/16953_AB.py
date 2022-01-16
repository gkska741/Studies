from typing import Collection


input = open('input.txt').readline
from collections import deque

A, B = map(int, input().split())

Q = deque()
Q.append(A)
times = 0
success = False
while Q:
    
    for _ in range(len(Q)):
        X = Q.popleft()

        if X == B:
            print(times+1)
            success = True
            break 

        if 2*X <= B:
            Q.append(2*X)
        
        if int(str(X) + '1') <= B:
            Q.append(int(str(X) + '1'))
    times += 1

if not success:
    print(-1)