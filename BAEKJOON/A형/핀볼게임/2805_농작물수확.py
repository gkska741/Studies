input = open('input.txt').readline
import time

start = time.time()
TC = int(input())

for tc in range(TC):
    N = int(input())
    board = [list(map(int, input().strip())) for _ in range(N)]
    
    initial = (N-1)//2

    value = 0
    for i in range(N):
        x = initial - abs(i-initial)
        value += sum(board[i][initial-x:initial+x+1]) 
    print(f'#{tc + 1} {value}')

print(time.time() - start)