from collections import deque
from pprint import pprint
board = [[0] * 4 for _ in range(3)]
board[1][1] = 1

dc = [0, 0, -1, 1]
dr = [1, -1, 0, 0]

def BFS():
    Q = deque()
    Q.append((1,1))
    cnt = 1
    while Q:
        temp = []
        cnt += 1
        while Q:
            c, r= Q.popleft()

            for i in range(4):
                new_c = c + dc[i]
                new_r = r + dr[i]

                if 0 <= new_c <= 2 and 0 <= new_r <= 3:
                    if board[new_c][new_r] == 0:
                        board[new_c][new_r] = cnt
                        temp.append((new_c, new_r))
        for x in temp:
            Q.append(x)
    return cnt
print(BFS()-1)
pprint(board)

    

