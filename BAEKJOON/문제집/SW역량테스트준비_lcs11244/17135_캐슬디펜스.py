input = open('input.txt').readline
from itertools import combinations
from collections import deque
from copy import deepcopy
dc = [0, -1, 0]
dr = [-1, 0, 1]
C, R, D = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]
archer_list = list(combinations(range(R), 3))
max_val = 0

def game(temp, archers):            
    column = C
    score = 0
    while column >= 0:
        for archer in archers:
            q = deque()
            q.append((column, archer))

            while q:
                distance = 1

                for _ in range(len(q)):
                    c, r = q.popleft()

                    for i in range(3):
                        nc = c + dc[i]
                        nr = r + dr[i]

                        if 0 <= nc < C and 0 <= nr < R:
                            


        column -= 1
    return score
        

    

for archers in archer_list:
    temp = deepcopy(board)

    score = game(temp, archers)
    max_val = max(score, max_val)

print(max_val)



