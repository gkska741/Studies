input = open('input.txt').readline

def dijstra():
    pass

TC = int(input())
for tc in range(1, TC+1):
    N, M, X = map(int, input().split())

    adj1 = [[0xffffff] * (N+1) for _ in range(N+1)]
    adj2 = [[0xffffff] * (N+1) for _ in range(N+1)]

    for _ in range(m):
        x, y, c = map(int, input().split())
        adj1[x][y] = c
        adj2[x][y] = c

    dist1 = [0xffffff] * (N+1)
    dist2 = [0xffffff] * (N+1)

    max_value = 0

    for i in range(1, N+1):
        if dist1[i] + dist2[i] > max_value:
            max_value = dist1[i] + dist2[i]

    print(tc, max_value)