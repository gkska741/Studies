input = open('input.txt').readline
from collections import deque
TC = int(input())


def BFS():
    Q = deque()
    for i in range(M):
        Q.append(board[i])

    friends = [0] * (N+1)
    friends[1] = 0

    cnt = 0
    group_numbering = 0
    while Q:
        a, b = Q.popleft()
        if friends[a] and friends[b]:
            if friends[a] != friends[b]:
                cnt -=1
        elif friends[a] or friends[b]:
            if friends[a]:
                friends[b] = friends[a]
            else:
                friends[a] = friends[b]
        else:
            cnt += 1
            group_numbering += 1
            friends[a] = friends[b] = group_numbering
    return cnt
    

for tc in range(1, TC+1):
    N, M = map(int, input().split())

    board = [sorted(tuple(map(int, input().split()))) for _ in range(M)]
    board.sort(key= lambda x : x[0])
    print(f'#{tc} {BFS()}')

    



        
        


