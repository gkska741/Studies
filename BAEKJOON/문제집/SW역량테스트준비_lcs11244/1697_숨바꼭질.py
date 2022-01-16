input = open('input.txt').readline
from collections import deque

def bfs():
    q = deque()
    q.append(N)

    while q:
        x = q.popleft()
        if x == K:
            print(dist[K])
            break

        for nx in (x-1, x+1, 2*x):
            if 0 <= nx <= MAX and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


N, K = map(int, input().split())
MAX = 10**5
dist = [0] * (MAX+1)
bfs()