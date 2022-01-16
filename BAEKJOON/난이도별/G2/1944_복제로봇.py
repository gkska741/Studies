input = open('input.txt').readline
from itertools import combinations

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def find_set(x):
    while x != p[x]: x = p[x]
    return x

def Union(a, b):
    root_a, root_b = find_set(a), find_set(b)
    p[root_a] = root_b

def bfs(c, r, c2, r2):
    length = 0
    Q = [(c, r)]

    while Q:
        temp = []
        while Q:
            c, r = Q.pop()
            if c == c2 and r == r2:
                return length
            visited[c][r] = 1

            for i in range(4):
                nc = c + dc[i]
                nr = r + dr[i]  

                if 1 <= nc <= N-2 and 1 <= nr <= N-2:
                    if board[nc][nr] != '1' and visited[nc][nr] == 0:
                        temp.append((nc, nr))
    
                    


        for x in temp:
            Q.append(x)
        length += 1
N, K = map(int, input().split())
board = [list(map(str, input().strip())) for _ in range(N)]
keys = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'S' or board[i][j] == 'K':
            keys.append((i, j))


G_list = list(combinations(keys, 2))
index_list = list(range(1, len(keys)+1))
index_list = list(combinations(index_list, 2))
G = []
while G_list:
    two_points = G_list.pop()
    u, v = index_list.pop()

    c1, r1 = two_points[0]
    c2, r2 = two_points[1]

    visited = [[0] * N for _ in range(N)]
    length = bfs(c1, r1, c2, r2)

    

    G.append((u, v, length))
G.sort(key=lambda x : x[2])

p = [i for i in range(len(keys) + 1)]

result = 0
cnt = 0
for u, v, val in G:
    if find_set(u) != find_set(v):
        Union(u, v)
        result += val
        cnt += 1

        if cnt == K:
            break
print(result)





