import sys
sys.stdin = open('input.txt')

TC = int(input())
for tc in range(1, TC+1):
    lst = list(map(int, input().split()))

    n = lst[0]
    cnt = 0
    i = 1

    while n > 1:
        if i + lst[i] >= n:
            n = i
            cnt += 1
            i = 1
        else:
            i += 1
    print(f'#{tc} {cnt-1}')

    
        

