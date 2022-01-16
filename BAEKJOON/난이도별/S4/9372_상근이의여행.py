input = open('input.txt').readline

TC = int(input())

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x


for i in range(TC):
    N, M = map(int, input().split())
    p = [i for i in range(N+1)]
    cnt = 0
    for _ in range(M):
        a, b = map(int, input().split())

        root_a = find_set(a); root_b = find_set(b)
        if root_a != root_b:
            cnt += 1
            p[root_a] = root_b
    print(cnt)
