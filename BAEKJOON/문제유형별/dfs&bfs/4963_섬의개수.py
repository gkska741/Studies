input = open('input.txt').readline
from collections import deque

dc = [-1, -1, -1, 0, 0, 1, 1, 1]
dr = [1, 0, -1, -1, 1, -1, 0, 1]


def bfs(c, r):
    q = deque()
    q.append((c, r))
    
    while q:

        c, r = q.popleft()

        board[c][r] = 0
        for i in range(8):
            nc = c + dc[i]; nr = r + dr[i]
            if 0 <= nc < C and 0 <= nr < R:
                if board[nc][nr] == 1:
                    q.append((nc, nr))
    
while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0:
        break

    board = [list(map(int, input().split())) for _ in range(C)]

    land_count = 0
    for c in range(C):
        for r in range(R):
            if board[c][r]:
                land_count += 1
                bfs(c, r)

    print(land_count)




def dfs(x, y):
  dx = [1, 1, -1, -1, 1, -1, 0, 0]
  dy = [0, 1, 0, 1, -1, -1, 1, -1]

  field[x][y] = 0
  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 0 <= nx < h and 0 <= ny < w and field[nx][ny] == 1:
      dfs(nx, ny)

while True:
  w, h = map(int, input().split())
  if w == 0 and h == 0:
    break
  field = []
  count = 0
  for _ in range(h):
    field.append(list(map(int, input().split())))
  for i in range(h):
    for j in range(w):
      if field[i][j] == 1:
        dfs(i, j)
        count += 1
  
  print(count)
