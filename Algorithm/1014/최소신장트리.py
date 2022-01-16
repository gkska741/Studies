input = open('input.txt').readline

TC = int(input())

for tc in range(1, TC+1):
    V, E = map(int, input().split())
    edges = []
    for _ in range(E):
        edges.append(tuple(map(int, input().split())))

    p = [i for i in range(V + 1)]
    def find_set(x):
        if x != p[x]: 
            p[x] = find_set(p[x])
        return p[x]

    #========================================
    # 가중치 내림차순으로 정렬
    edges.sort(key=lambda x: x[2], reverse=True)
    ans = 0
    # 싸이클이 생기지 않도록 V개의 간선을 선택
    cnt = V
    while cnt:
        u, v, w = edges.pop()
        a = find_set(u)
        b = find_set(v)
        if a == b: continue
        p[b] = a
        ans += w
        cnt -= 1
    print(ans)