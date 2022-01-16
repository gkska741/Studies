from pprint import pprint
from types import TracebackType
input = open('input.txt').readline

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(C)]
status = [[] for _ in range(7)]

dc = [-1, 0, 1, 0]
dr = [0, 1, 0, -1]

for c in range(C):
    for r in range(R):

        if board[c][r]:
            status[board[c][r]].append((c, r))

def case(index, board):
    if not status[index]:
        return board
    
    if index == 5:
        while status[index]:
            c, r = status[index].pop()
            
            for i in range(4):
                tc, tr = c, r
                
                while True:
                    tc += dc[i]; tr += dr[i]
                    
                    if 0 <= tc <= C-1 and 0 <= tr <= R-1:
                        if board[tc][tr] == 6:
                            break

                        if board[tc][tr] == 0:
                            board[tc][tr] = '#'
                    else:
                        break

    if index == 4:
        while status[index]:
            c, r = status[index].pop()
            dev = [0] * 4
            for i in range(4):
                tc, tr = c+dc[i], r+dr[i]
                
                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        dev[i] += 1
                    tc += dc[i]; tr += dr[i]
            except_index = dev.index(min(dev))
            
            for i in range(4):
                if i == except_index:
                    continue

                tc, tr = c + dc[i], r + dr[i]

                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        board[tc][tr] = '#'
                    tc += dc[i]; tr += dr[i]

    if index == 3:
        while status[index]:
            c, r = status[index].pop()
            dev = [0] * 4
            for i in range(4):
                tc, tr = c+dc[i], r+dr[i]
                
                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        dev[i] += 1
                    tc += dc[i]; tr += dr[i]

            new_dev = [dev[0] + dev[1], dev[1] + dev[2], dev[2] + dev[3], dev[3] + dev[0]]
            new_dev_index = [[0, 1], [1, 2], [2, 3], [3, 0]]
            correct_index = new_dev_index[new_dev.index(max(new_dev))]


            for i in range(4):
                if i in correct_index:
                    tc, tr = c + dc[i], r + dr[i]

                    while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                        if board[tc][tr] == 6:
                            break

                        if board[tc][tr] == 0:
                            board[tc][tr] = '#'
                        tc += dc[i]; tr += dr[i]
                else: continue


    if index == 2:
        while status[index]:
            c, r = status[index].pop()
            dev = [0] * 4
            for i in range(4):
                tc, tr = c+dc[i], r+dr[i]
                
                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        dev[i] += 1
                    tc += dc[i]; tr += dr[i]
            if dev[0] + dev[2] > dev[1] + dev[3]:
                except_index = [1, 3]
            else:
                except_index = [0, 2]
            for i in range(4):
                if i in except_index:
                    continue

                tc, tr = c + dc[i], r + dr[i]

                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        board[tc][tr] = '#'
                    tc += dc[i]; tr += dr[i]

    if index == 1:
        while status[index]:
            c, r = status[index].pop()
            dev = [0] * 4
            for i in range(4):
                tc, tr = c+dc[i], r+dr[i]
                
                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        dev[i] += 1
                    tc += dc[i]; tr += dr[i]
            correct_index = dev.index(max(dev))
            
            for i in range(4):
                if i != correct_index:
                    continue

                tc, tr = c + dc[i], r + dr[i]

                while 0 <= tc <= C-1 and 0 <= tr <= R-1:
                    if board[tc][tr] == 6:
                        break

                    if board[tc][tr] == 0:
                        board[tc][tr] = '#'
                    tc += dc[i]; tr += dr[i]

    return board


for index in range(5, 0, -1):
    board = case(index, board)

answer = 0
for c in range(C):
    for r in range(R):
        if board[c][r] == 0:
            answer += 1

print(answer)


