input = open('input.txt').readline

def calc(n, idx):
    if idx == 0 : return n+1
    elif idx == 1: return n-1
    elif idx == 2: return n*2
    else: return n-10


def BFS():
    Q = [0] * 1000000
    
    front = rear = -1
    
    rear += 1
    Q[rear] = N
    memo[N] = 0

    while front != rear:
        front += 1
        num = Q[front]

        if num == M:
            return memo[num]
        
        for i in range(4):
            next_num = calc(num, i)

            if 0 < next_num <= 1000000 and memo[next_num] == -1:
                memo[next_num] = memo[num] + 1
                rear += 1
                Q[rear] = next_num
            
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    memo = [-1] * 1000001
    print(f'#{tc} {BFS()}')

#--------------------------------------------------------------------------------------------

from collections import deque

def BFS():
    Q = deque()
    Q.append(N)
    memo[N] = True
    ans = 0

    while Q:
        size = len(Q)

        for i in range(size):
            num = Q.popleft()
            if num == M: return ans

            for j in (num+1, num-1, num*2, num-10):
                if 0 < j <= 1000000 and not memo[j]:
                    memo[j] = True
                    Q.append(j)
        ans += 1

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    memo = [False] * 1000001


