input = open('input.txt').readline
n = int(input())

mat = []
for i in range(n):
    mat.append(list(map(int, input().split())))

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for y in range(n):
    for x in range(n):
        if mat[y][x] == 0:
            break
        nx = x + mat[y][x]
        ny = y + mat[y][x]
        if 0 <= nx < n:
            dp[y][nx] += dp[y][x]
        if 0 <= ny < n:
            dp[ny][x] += dp[y][x]
print(dp[-1][-1])