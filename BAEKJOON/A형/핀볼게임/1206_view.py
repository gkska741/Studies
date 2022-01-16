input = open('input.txt').readline

TC = 10

for tc in range(1, TC+1):
    length = int(input())
    board = list(map(int, input().split()))
    
    cnt = 0
    for i in range(2, length-2):
        height = board[i]
        lst = [height - board[i-1], height - board[i-2], height - board[i+1], height - board[i+2]]
        jomang = min(lst)
        if jomang >= 1:
            cnt += jomang
    
    print(f'#{tc} {cnt}')
            