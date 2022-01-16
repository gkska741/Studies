from itertools import permutations
input = open('input.txt').readline

def deepcopy(map):
    map = [[] for _ in range(H)]
    for i in range(H):
        for j in range(W):
            map[i][j] = board[i][j]
    return board

def drop(bomb_list, board):
    pass





TC = int(input())

for tc in range(1):
    N, W, H = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(H)]
    bomb_list = list(permutations(list(range(W)), N))

    intial_map = deepcopy(board)