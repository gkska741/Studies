input = open('input.txt').readline
from pprint import pprint
N, V = map(int, input().split())

dp = [[0] * (V+1) for _ in range(N+1)]
m = [[0, 0]]

for i in range(N):
    w, v = map(int, input().split())
    m.append([w, v])

for i in range(1, N+1):
    w = m[i][0]
    v = m[i][1]

    for j in range(1, V+1):
        if j < w:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

pprint(dp)
print(dp[N][V])
