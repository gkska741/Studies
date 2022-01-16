import sys
sys.stdin = open('input.txt')

def calc(cost, m):
    global min_cost
    if m > 12:
        if min_cost > cost:
            min_cost = cost
        return
    calc(cost + d * month[m], m + 1)
    calc(cost + m1, m + 1)
    calc(cost + m3, m + 3)

T = int(input())

for tc in range(1, T+1):
    d, m1, m3, y = map(int, input().split())
    month = [0] + list(map(int, input().split()))

    min_cost = y

    calc(0, 1)
    print(f'#{tc} {min_cost}')