input = open('input.txt').readline

N, E = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((v, w))

D = [0xffffff] * (N+1)
Q = [0]
D[0] = 0


while Q:
    u = Q.pop(0)

    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            Q.append(v)

#--------------------------------------------------------------------

def dfs(u):
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            dfs(v)


#---------------------------------------------------------------
D = [0xffffff] * (N+1)
visit = [0] * (N+1)
cnt = N+1

while cnt:

    u, min_val = 0, 0xfffffff

    for i in range(N+1):
        if visit[i] == 0 and min_val > D[i]:
            u, min_val = i, D[i]
    visit[u] = 1
    
    for v, w in G[u]:
        if D[v] > D[u] + w:
            D[v] = D[u] + w
            Q.append(v)
    cnt -= 1


