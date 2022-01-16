import sys
sys.stdin = open('12398_input.txt')

TC = int(input())

def dfs(S, visited, board):
    visited[S] = 1
    for node in board[S]:
        if visited[node] != 1:
            dfs(node, visited, board)

for tc in range(TC):
    V, E = map(int, input().split())
    board = [[]*(V+1) for _ in range(V+1)]
    for j in range(E):
        x, y = map(int, input().split())
        board[x].append(y)

    S, G = map(int, input().split())
    visited = [0 for _ in range(V+1)]

    dfs(S, visited, board)
    answer = 0
    if visited[G] == 1:
        answer = 1

    print(f'#{tc + 1} {answer}')




