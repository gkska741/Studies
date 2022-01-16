input = open('input.txt').readline
from collections import deque
N, M = map(int, input().split())

LS = {}
for _ in range(N+M):
    start, end = map(int, input().split())
    LS[start] = end

dice = [1, 2, 3, 4, 5, 6]
visited = [0]*101
Q = deque()
Q.append(1)
times = 0
while Q:
    for _ in range(len(Q)):
        now = Q.popleft()
        if now == 100:
            print(times)
            break
        for i in range(6):
            new_location = now + dice[i]
            if new_location <= 100:
                if LS.get(new_location) != None:
                    if not visited[LS[new_location]]:
                        visited[LS[new_location]] = 1
                        Q.append(LS[new_location])
                else:
                    if not visited[new_location]:
                        visited[new_location] = 1
                        Q.append(new_location)
    if now == 100:
        break
    times += 1



