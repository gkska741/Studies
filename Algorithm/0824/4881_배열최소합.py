import sys
sys.stdin = open('4881_input.txt')

def perm(k, cur_sum):
    global ans
    if cur_sum >= ans:
        if k == N:
            if ans > cur_sum:
                ans = cur_sum
    else:
        for i in range(k, N):
            cols[k], cols[i] = cols[i], cols[k]
            perm(k + 1, cur_sum + arr[k][cols[k]])
            cols[k], cols[i] = cols[i], cols[k]

N = 3
cols = [i for i in range(N)]
ans = 10000
perm(0,0)


TC = int(input())

for case_number in range(1, TC+1):
    size = int(input())
    board = [list(map(int, input().split())) for _ in range(size)]







