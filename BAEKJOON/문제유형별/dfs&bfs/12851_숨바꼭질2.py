input = open('input.txt').readline
from collections import deque
N, M = map(int, input().split())

def bfs(n):
    q = deque([N])

    visited[n][0] = 0
    visited[n][1] = 1

    while q:
        x = q.popleft()

        for i in [x-1, x+1, x*2]:
            if 0 <= i <= 100000:
                if visited[i][0] == -1:
                    visited[i][0] = visited[x][0] + 1
                    visited[i][1] = visited[x][1]
                    q.append(i)

                elif visited[i][0] == visited[x][0] + 1:
                    visited[i][1] += visited[x][1]



visited = [[-1, 0] for _ in range(100001)]
bfs(N)
print(visited[M][0])
print(visited[M][1])