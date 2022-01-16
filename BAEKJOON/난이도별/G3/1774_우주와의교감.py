input = open('input.txt').readline
from itertools import combinations

def Find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def Union(x, y):
    root_x, root_y = Find_set(x), Find_set(y)
    p[max(root_x, root_y)] = min(root_x, root_y)

def KRUSKAL(G):

    mst_cost = 0
    while len(mst) < N-1:
        u, v, val = G.pop()
        if Find_set(u) != Find_set(v):
            Union(u, v)
            mst_cost += val
            mst.append((u, v))

    return mst_cost

N, M = map(int, input().split())
gods = []
p = [i for i in range(N+1)]
for i in range(N):
    god_x, god_y = tuple(map(int, input().split()))
    gods.append((god_x, god_y, i+1))

lines = list(combinations(gods, 2))
G = []
mst = []

while lines:
    two_gods = lines.pop()
    distance = ((two_gods[0][0]-two_gods[1][0])**2 + (two_gods[0][1]-two_gods[1][1])**2)**0.5
    new_info = (two_gods[0][2], two_gods[1][2], distance)
    G.append(new_info)

for _ in range(M):
    i_1, i_2 = map(int, input().split())
    Union(i_1, i_2)
    mst.append((i_2, i_1))

G.sort(key=lambda x : x[2], reverse=True)

value = '{:.2f}'.format(KRUSKAL(G))
print(value)
