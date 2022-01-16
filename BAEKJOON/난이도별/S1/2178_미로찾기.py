input = open('input.txt').readline
from collections import deque
N, M = map(int, input().strip().split())
board = [list(map(int, input().strip())) for _ in range(N)]

sc = 0; sr = 0
ec = N-1; er = M-1

dr = [0, 0, -1, 1]
dc = [1, -1, 0, 0]

visited = [[False] * M for _ in range(N)]
visited[0][0] = True

def BFS():
    cnt = 1
    Q = deque()
    Q.append((sc, sr))

    while Q:
        temp = []
        while Q:
            c, r = Q.popleft()
            for i in range(4):
                new_r = r + dr[i]
                new_c = c + dc[i]
                if 0 <= new_r <= er and 0 <= new_c <= ec:
                    if board[new_c][new_r] and not visited[new_c][new_r]:
                        if (new_c, new_r) == (N-1, M-1):
                            return cnt + 1
                        else:
                            temp.append((new_c, new_r))
                            visited[new_c][new_r] = True
        for x in temp:
            Q.append(x)

        cnt += 1
    return cnt

result = BFS()
print(result)
