input = open('input.txt').readline

N, r, c = map(int, input().split())


board = [[0]* 2**N for _ in range(2**N)]

small_Z = [[0, 1], [1, -1], [0, 1]]


cnt = 0

def dfs(N, m):
    print(f'dfs{N}, {m}')
    global cnt
    if N == 1:
        pass

    else:
        for i in range(4):
            dfs(N-1, i)


dfs(N, 0)