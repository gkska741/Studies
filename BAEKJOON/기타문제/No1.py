input = open('input.txt').readline
from collections import deque
TC = int(input())

dc = [1, -1, 0, 0]
dr = [0, 0, -1, 1]

for case_number in range(TC):
    C, R, L = map(int, input().split())

    def find_lock_in_L(c, r):
        result = []
        dist = 0


        Q = deque()
        Q.append((c, r))

        while Q and dist < L:
            temp = []

            while Q:
                c, r = Q.pop()
                for i in range(4):
                    nc = c + dc[i]
                    nr = r + dr[i]

                    if 0 <= nc <= C-1 and 0 <= nr <= R-1:
                        if board[nc][nr] == 1:
                            if not visited[nc][nr]:
                                visited[nc][nr] = 1
                                result.append((nc, nr))
                                
                        
                        if board[nc][nr] == 3:
                            result.append((nc, nr))

                        temp.append((nc, nr))

            for xy in temp:
                Q.append(xy)
            dist += 1
        if result:
            return result
        
        return []


    def bfs(c, r):
        tries = 0
        Q = deque()
        Q.append((c, r))
        
        while True:
            temp = []
            while Q:
                c, r = Q.pop()
                locks = find_lock_in_L(c, r)
               
                temp += locks


            if (end_c, end_r) in temp:
                return tries
            
            if not temp:
                return -1

            for x in temp:
                Q.append(x)
            tries += 1

    board = [list(map(int, input().split())) for _ in range(C)]
    visited = [[0] * R for _ in range(C)]
    
    for c in range(C):
        for r in range(R):
            if board[c][r] == 3:
                end_c = c
                end_r = r
            
            if board[c][r] == 2:
                start_c = c
                start_r = r

    print(f'#{case_number+1} {bfs(start_c, start_r)}')
    