import sys
from pprint import pprint
sys.stdin = open('1219_input.txt')

def dfs(S, visited, board):
    visited[S] = 1
    for node in board[S]:
        if visited[node] != 1:
            dfs(node, visited, board)

for tc in range(10):
    case_number, lines = map(int, input().split())
    sequence = list(map(int, input().split()))

    board = [[] for _ in range(100)]
    for i in range(0, len(sequence), 2):
        board[sequence[i]].append(sequence[i+1])

    visited = [0 for _ in range(100)]
    S, G = 0, 99
    answer = 0
    dfs(S, visited, board)

    if visited[99] == 1:
        answer = 1

    print(f'#{case_number} {answer}')





