input = open('input.txt').readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

result = 0

def dfs(i, graph, total):
    global result

    if total == S:
        result += 1

    for j in range(i+1, N):
        dfs(j, graph, total + graph[j])

for i in range(N):
    dfs(i, numbers, numbers[i])

print(result)