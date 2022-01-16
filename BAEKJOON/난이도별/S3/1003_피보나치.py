

memo = [[1, 0], [0, 1]] 
def fibo(n):
    global memo

    if n >= 2 and len(memo) <= n:
        memo.append([(fibo(n-1)[0] + fibo(n-2)[0]), (fibo(n-1)[1] + fibo(n-2)[1])])

    return memo[n]

TC = int(input())

for _ in range(TC):
    n = int(input())
    fibo(n)
    print(memo[n][0], memo[n][1])
