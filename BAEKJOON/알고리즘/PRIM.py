N = 5

def MST_PRIM(G, s):

    key = [0xffffff] * N
    pi = [None]*N

    visited = [False] * N
    key[s] = 0

    for _ in range(N):
        minIndex = -1
        min = 0xffffff

        for i in range(N):  
            if not visited[i] and key[i] <min: 
                min = key[i]
                minIndex = i
        visited[minIndex] = True

        for v, val in G[minIndex]:
            if not visited[v] and val < key[v]:
                key[v] = val
                pi[v] = minIndex

''' 
    1. 0번 정점부터 시작해서 인접 정점들 중에 가장 가중치가 낮은 간선과 그 간선의 도착점에 해당하는 노드를 선택

    2. 선택된 노드와 연결된 모든 인접 정점과 간선을 다시 비교할 대상에 추가

    3. 간선들 중 가장 낮은 가중치를 가진 간선과 노드를 선택

    4. 모든 정점이 선택될 때까지 반복

'''