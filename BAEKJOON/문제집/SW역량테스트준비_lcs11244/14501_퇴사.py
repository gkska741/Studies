input = open('input.txt').readline


N = int(input())

table = [[0] * N for _ in range(2)]

for i in range(N):
    day, cost = map(int, input().split())
    table[0][i] = day
    table[1][i] = cost

value = 0
max_val = 0
dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    
    if i + table[0][i] > N:
        dp[i] = dp[i+1]

    else:
        dp[i] = max(table[1][i] + dp[i+table[0][i]], dp[i+1])
        if max_val < dp[i]:
            max_val = dp[i]
print(max_val)