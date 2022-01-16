from itertools import combinations
input = open('input.txt').readline
#큰 정사각형 형태를 어떻게 처리할 것인가?

TC = int(input())


direction = [[1, 1], [1, -1]] # 0-오른쪽, 1-왼쪽
sur = [[1, 0], [0, -1], [-1, 0], [0, 1]] # 하, 좌, 상, 우
def can_loop(i, j, direction):
    global dp_memo

    if not dp_memo:
        for k in range(4):
            new_i = i + sur[k][0]
            new_j = j + sur[k][1]
            value = board[new_i][new_j]
            dp_memo.append(value)
        
        if len(set(dp_memo)) != 4:
            return False

    else:
        if direction == 'right':
            for index in [0, 3]:
                new_i = i + sur[index][0]
                new_j = j + sur[index][1]

                value = board[new_i][new_j]
                if value in dp_memo:
                    return False
                dp_memo.append(value)
        
        elif direction == 'left':
            for index in [0, 1]:
                new_i = i + sur[index][0]
                new_j = j + sur[index][1]

                value = board[new_i][new_j]
                if value in dp_memo:
                    return False
                dp_memo.append(value)

    return True

def calculate(i, j):
    global dp_memo, cnt_left, cnt_right
    initial_i = i
    initial_j = j

    while 0 < i < N-1 and 0 < j < N-1:
        is_good = can_loop(i, j, 'right')
        if not is_good:
            break
        else:
            cnt_right += 1
            i += direction[0][0]
            j += direction[0][1]

    dp_memo = []

    i = initial_i 
    j = initial_j   
    while 0 < i < N-1 and 0 < j < N-1:
        is_good = can_loop(i, j, 'right')
        if not is_good:
            break
        else:
            cnt_left += 1
            i += direction[1][0]
            j += direction[1][1]
    return max(cnt_left, cnt_right)

for tc in range(3):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    # search_area : 1 ~ N-2 인덱스 범위
    # 최대 대각선의 길이(내부에 들어가는 디저트 카페의 최대 개수) : 1 ~ N-2
    max_val = 0
    for i in range(N):
        for j in range(N):
            dp_memo = []
            cnt_left = 0
            cnt_right = 0
            max_val = max(max_val, calculate(i, j))

    if max_val:
        print(f'#{tc+1} {max_val * 2 + 2}')
    else:
        print(f'#{tc+1} -1')
