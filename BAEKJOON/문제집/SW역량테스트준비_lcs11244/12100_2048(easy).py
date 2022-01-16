input = open('input.txt').readline
from collections import deque
from copy import deepcopy

dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

def move(board, di):
    # can_merged[i][j] 는 (i, j)번째 블록이 합쳐질 수 있는지를 bool 타입으로 담는다.
    can_merged = [[True] * n for _ in range(n)]

    # 움직이는 방향에 따라, 반복문의 진행방향이 다르다.
    # 위 또는 왼쪽으로 이동하는 경우
    if di in [0, 3]:
        start_idx, end_idx, step = 0, n, 1

    # 아래 또는 오른쪽으로 이동하는 경우
    else:
        start_idx, end_idx, step = n-1, -1, -1

    # 현재 판의 모든 좌표를 탐색하며, 움직임이 필요한 값들은 움직인다.
    for i in range(start_idx, end_idx, step):
        for j in range(start_idx, end_idx, step):
            if board[i][j] == 0:
                continue

            x, y = i, j
            value = board[x][y]
            board[x][y] = 0
            nx, ny = x + dxs[di], y + dys[di]
            while True:
                # 범위 체크
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                # 다음 이동 좌표(nx, ny)가 비어있는 경우, 현재 좌표(x, y)를 이동.
                if board[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dxs[di], y + dys[di]

                # 다음 이동 좌표에 현재 이동하는 숫자와 같은 값인 경우, 해당 좌표를 합쳐진 상태로 바꾼다.
                elif board[nx][ny] == value and can_merged[nx][ny]:
                    x, y = nx, ny
                    can_merged[x][y] = False
                    break

                # 다음 이동 좌표가 비어있지도 않고, 같은 값도 아닌 경우, 움직임 종료.
                else:
                    break
            board[x][y] = board[x][y] + value

    return board

def bfs(board):
    """ 알고리즘 간략 설명
    1. bfs queue 에다가, 각 스텝에 따른 판 전체(board)를 집어넣는다.
    2. queue 에서 판을 하나씩 빼와, 4가지 방향으로 움직인 후의 판을 queue에 집어 넣는다.
    3. 스텝이 5번 째가 되었을 때, bfs 를 강제 종료.
    """
    q = deque([board])
    max_value = -1
    step = 0

    while q:
        size = len(q)

        for _ in range(size):
            board = q.popleft()

            for di in range(4):
                # 새로운 판을 만들어야 하므로, 반드시 deepcopy 해야한다!
                next_board = move(deepcopy(board), di)
                q.append(next_board)

                # 새로 만든 판에서 가장 큰 값을 조사한다.
                for i in range(n):
                    for j in range(n):
                        if next_board[i][j] > max_value:
                            max_value = next_board[i][j]      

        step += 1

        # 다섯 번째 스텝일 때, 지금까지 가장 큰 값을 반환한다.
        if step == 5:
            return max_value

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

print(bfs(board))