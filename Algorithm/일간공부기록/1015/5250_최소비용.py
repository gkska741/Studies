dr = [0, 0, 1, -1]
dc = [-1, 1, 0, 0]
def BFS():
    Q = [0] * 100000
    front = rear = -1

    rear += 1
    Q[rear] = (0, 0)

    while front != rear:
        front += 1
        r, c = Q[front]

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < N:
                power = arr[nr][nc] - arr[r][c] if arr[nr][nc] > arr[r][c] else 0

                if dist[nr][nc] > dist[r][c] + power + 1:
                    rear += 1
                    Q[rear] = (nr, nc)
                    dist[nr][nc] = dist[r][c] + power + 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())

    arr = [list(map(int, input().split())) for _ in range(N)]
    dist = [[0xffffff] * N for _ in range(N)]
    dist[0][0] = 0

    BFS()
    print(tc, dist[N-1][N-1])