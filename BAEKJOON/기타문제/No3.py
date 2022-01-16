input = open('input.txt').readline
from collections import deque
from itertools import permutations
TC = int(input())

dr = [1, -1]

def optimize_hunt_time(now_loc, fishes):
    if now_loc == -1:
        return fishes[-1], max(fishes)+2
    if len(fishes) == 1:
        return fishes[0], abs(fishes[0] - now_loc)+1


    min_time = 0xffffff
    possible_list = list(permutations(fishes, len(fishes)))
    for tuple in possible_list:
        temp = 0
        sequence = ([now_loc]+list(tuple))

        for i in range(len(sequence)-1):
            temp += abs(sequence[i] - sequence[i+1])
        if min_time > temp:
            min_time = temp
            result_loc = sequence[-1]
    return result_loc, temp



for case_number in range(1,TC+1):
    C, R = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(C)]

    for c in range(C):
        for r in range(R):
            if board[c][r] == 2:
                
                if c < C-1:
                    for nc in range(c, C):
                        if board[nc][r] == 1:
                            board[nc][r] = 0
                board[c][r] = 0


    depth = 0

    total_time = 0
    now_loc = -1

    eat_fishes = 0
    for c in range(C):
        if sum(board[c]):

            if c > eat_fishes:
                break
            fishes = []
            for r in range(R):
                if board[c][r] == 1:
                    fishes.append(r)

            now_loc, min_time = optimize_hunt_time(now_loc, fishes)
            eat_fishes += sum(board[c])
            total_time += min_time

    print(f'#{case_number} {total_time}')
