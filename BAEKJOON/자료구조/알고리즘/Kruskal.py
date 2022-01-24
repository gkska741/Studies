N = 5

def MST_KRUSKAL(G):
    mst = []

    for i in range(N):
        Make_set(i)
        rank[i] = 0

    G.sort(key = lambda x : x[2])

    mst_cost = 0

    while len(mst) <= N-1:
        u, v, val = G.pop(0)

        if Find_set(u) != Find_set(v):
            Union(u, v)
            mst.append((u, v))
            mst_cost += val

def Make_set(x):
    p[x] = x
    rank[x] = 0

def Find_set(x):
    if x == p[x]: return x
    else: return Find_set(p[x])

# def Find_set(x):
#     while x != p[x]: x = p[x]
#     return x

def Union(x, y):
    Link(Find_set(x), Find_set(y))

def Link(x, y):
    if rank[x] > rank[y]:
        p[y] = x
    else:
        p[x] = y
        if rank[x] == rank[y]:
            rank[y] += 1



p = [0] * N
rank = 