
N, M = map(int, input().split())
arr = list(map(int, input().split()))


p = [i for i in range(N+1)]

def find_set(x):
    if x != p[x]:
        p[x] = find_set(p[x])
    return p[x]

ans = N
for i in range(0, len(arr), 2):
    x, y = arr[i], arr[i+1]
    a = find_set(x)
    b = find_set(y)
    
    if a == b: continue
    p[b] = a
    ans -= 1

print(ans)