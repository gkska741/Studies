import sys
sys.stdin = open('input.txt')


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

pipe = [
    [0, 0, 0, 0],
    [1, 1, 1, 1],
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [1, 0, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
]
T = int(input())

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    Q = [(R, C)]
    visited[R][C] = 1

    ans = 0

    while Q:
        r, c = Q.pop()
        ans += 1
        if visited[r][c] >= L : continue

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if nr < 0 or nr >= N or nc < 0  or nc >= M: continue

            if pipe[tunnel[r][c]][d] == 0: continue

            nd = (d + 2) % 4
            np = tunnel[nr][nc]

            if visited[nr][nc] or pipe[np][nd] == 0: continue

            visited[nr][nc] = visited[r][c] + 1
            Q.append((nr, nc))

    print(f'#{tc} {ans}')