
'''
7 8
1 2 1 3 2 4 2 5 4 6 5 6 6 7 3 7

7 8
1 2 1 3 2 4 5 2 4 6 6 5 6 7 7 3
'''


def bfs(s, V):
    q = [0] * V
    front = -1
    rear = -1
    visited = [0] * (V+1)

    rear += 1
    q[rear] = s
    visited[s] = 1

    while front != rear:
        front += 1
        t = q[front]
        print(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                rear += 1
                q[rear] = 1
                visited[i] = visited[t] + 1


V, E = map(int, input().split())
edge = list(map(int, input().split()))
adj = [[0] * (V+1) for _ in range(V+1)]
adjlist = [[] for _ in range(V+1)]

for i in range(E):
    n1, n2 = edge[2 * i], edge[2*i + 1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1

    adjlist[n1].append(n2)
    adjlist[n2].append(n1)

bfs(1, V)