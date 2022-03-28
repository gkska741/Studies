input = open('input.txt').readline

from pprint import pprint
R, C = map(int, input().split())

board = []
total = 0
for _ in range(R):
    row = list(map(int, input().split()))
    total += sum(row)
    board.append(row)

pprint(board)
    
