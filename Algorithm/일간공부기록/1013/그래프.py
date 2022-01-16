input = open('input.txt').readline

def dfs(idx, ans):
    global answer
    visited[idx] = 0
    
    ans += 1
    if answer < ans: 
        answer = ans

    for i in graph[idx]:
        if visited[i]: dfs(i, ans)
    visited[idx] = 1
 
for t in range(1, int(input()) + 1):

    N, M = map(int, input().split())
    
    visited = [1 for _ in range(N+1)]
    temp = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    answer = 0

    for a, b, in temp:
        graph[a].append(b)
        graph[b].append(a)
    for i in range(N): 
        dfs(i, 0)
    print(f'{t} {answer}')