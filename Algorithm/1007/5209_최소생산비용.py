import sys
sys.stdin = open('input.txt')


TC = int(input())


def checknode(index, value):
    global max_value

    if value >= max_value:
        return
    if index == N:
        max_value = value
    
    for i in range(N):
        if visited[i]:
            visited[i] = 0
            checknode(index + 1, value + board[index][i])
            visited[i] = 1

for tc in range(1, TC +1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_value = 99 * N**2
    visited = [1] * (N+1)
    checknode(0, 0)
    print(f'#{tc} {max_value}')
    










#---------------------------------------------------------------------#
# from itertools import permutations
# TC = int(input())

# for tc in range(1, TC+1):
#     N = int(input())
#     board = [list(map(int, input().split())) for _ in range(N)]

#     arr = list(range(1, N+1))
#     temp = list(permutations(arr, N))

#     min_value = 10**5

#     for perms in temp:
#         value = 0
#         for i in range(N):
#             value += board[i][perms[i]-1]
#         min_value = min(value, min_value)
    
#     print(f'#{tc} {min_value}')



    
    