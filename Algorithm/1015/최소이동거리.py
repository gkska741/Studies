input = open('input.txt').readline



def dijstra():
    dist = [0xffffff] * (V+1)
    visited = [0] * (V+1)

    dist[0] = 0

    for _ in range(V):
        min_idx = -1
        min_value = 0xfffffff

        for i in range(V+1):
            if not visited[i] and min_value > dist[i]:
                min_idx = i
                min_value = dist[i]

        visited[min_idx] = 1

        for i in range(V+1):
            if not visited[i] and dist[i] > dist[min_idx] + adj_arr[min_idx][i]:
                dist[i] = dist[min_idx] + adj_arr[min_idx][i]

    return dist[V]



TC = int(input())

for tc in range(1, T+1):
    V, E = map(int, input().split())

    adj_arr = [[0xfffffff] *(V+1) for _ in range(V+1)]

    for i in range(E):
        s, e, w = map(int, input().split())
        adj_arr[s][e] = w
    print(tc, dijstra())