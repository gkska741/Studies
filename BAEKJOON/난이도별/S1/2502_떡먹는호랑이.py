import sys
sys.stdin = open('input.txt')

def fibo(n):
    global memo
    for i in range(2, n):
        memo.append(memo[i-1] + memo[i-2])

memo = [1, 1]


n, k = map(int, input().split())
fibo(n)

selection = []
if n > 4:
    for i in range(1, k+1):
        day1 = ((-1)**n) * memo[n-4]*k + ((-1)**(n-1))*memo[n-2]*i
        day2 = ((-1)**(n-1)) * memo[n-5]*k + ((-1)**n)*memo[n-3]*i
        if day1 > 0 and day2 > 0:      
            if day2-day1 > 0:
                selection.append(day1)
                selection.append(day2)
        if selection:
            break
    print(day1)
    print(day2)

elif n == 4:
    for i in range(1, k+1):
        if k - 2*i > 0:
            day1 = k-2*i
            day2 = i
    print(day1)
    print(day2)
else:
    day1 = k//2 
    day2 = k - day1
    print(day1)
    print(day2)
    