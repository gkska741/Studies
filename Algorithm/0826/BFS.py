#import sys
#sys.stdin = open('5102_input.txt')

V, E = map(int, input().split())
G = [[] for _ in range(V+1)]

for _ in range(E):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

visited = [0] * (V+1)
D = [0] * (V + 1) #시작점에서 최단 거리
P = [0] * (V + 1) #최단 경로
v = 1
Q = [v]
visited[v] = 0

while Q:
    v = Q.pop(0)
    for w in G[v]:
        if not visited[w]:
            Q.append(w)
            visited[w] = visited[v] + 1

print(visited)