# 이코드는 시간초과 코드입니다. dfs는 시간내에 풀방법이 없을까요?
import sys
sys.stdin = open('input.txt')


N, M = map(int, input().split())
board = [[] for _ in range(N+1)]
for i in range(M):
    e, s = map(int, input().split())
    board[s].append(e)

visited = [0]*(N+1)
cascade = [0] * (N+1)

def dfs(s):
    global count
    count +=1
    visited[s] = 1
    for e in board[s]:
        if not visited[e]:
            cascade[e] = 1
            dfs(e)

counts = [0] * (N+1)
i = 1
while sum(visited) + sum(cascade) != N:
    if visited[i] == 0 and cascade[i] == 0:
        temp = visited[::]
        count = 0
        dfs(i)
        counts[i] = count
        visited = temp[::]
        visited[i] = 1
    i += 1

max_cnt = max(counts)

for i in range(len(counts)):
    if counts[i] == max_cnt:
        print(i, end=' ')


    
