input = open('input.txt').readline

C, R = map(int, input().split())

board = [list(map(str, input().split())) for _ in range(C)]
throws = int(input())
height = list(map(int, input().split()))

all_minerals = 0
for c in range(C):
    for r in range(R):
        if board[c][r] == 'x':
            all_minerals += 1

print(all_minerals)


visited = [[0] * R for _ in range(C)]

for i in range(throws):
    get_min(throws[i])

    all_minerals -= 1
    local_minerals = 0

    for r in range(R):
        if board[C-1][r] == 'x':
            dfs(c, r)
    if local_minerals != all_minerals:
        


                


