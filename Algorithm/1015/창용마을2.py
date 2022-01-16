


result = []
input = open('input.txt').readline
TC = int(input())
for tc in range(1, TC+1):
    N, M = map(int, input().split())
    board = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        board[u].append(v)
        board[v].append(u)

    def DFS(v):
        visit[v] = 1
        for w in board[v]:
            if visit[w]: 
                continue
            DFS(w)
        
    visit = [0] * (N+1)
    cnt = 0
    for i in range(1, N+1):
        if visit[i]:
            continue
        cnt += 1
        DFS(i)
    result.append(f'#{tc} {cnt}')
print('\n'.join(result))
        


ans = []
for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    G = [[] for _ in range(N + 1)]
 
    for _ in range(M):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)
 
    def DFS(v):
        visit[v] = 1
        for w in G[v]:
            if visit[w]: continue
            DFS(w)
 
    visit = [0] * (N + 1)
    cnt = 0
    for i in range(1, N + 1):
        if visit[i]: continue
        cnt += 1
        DFS(i)
    ans.append('#{} {}'.format(tc, cnt))
print('\n'.join(ans))