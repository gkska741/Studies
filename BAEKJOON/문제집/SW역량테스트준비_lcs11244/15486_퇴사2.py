input = open('input.txt').readline


n = int(input())
t, p = [], []
dp = [0 for _ in range(n + 1)]

for _ in range(n):
    ti, pi = map(int, input().split())
    t.append(ti)
    p.append(pi)

k = 0
for i in range(n):
    k = max(k, dp[i])
    if i + t[i] > n:
        continue
    dp[i + t[i]] = max(k + p[i], dp[i + t[i]])

print(max(dp))