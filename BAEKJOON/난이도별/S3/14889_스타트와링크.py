input = open('input.txt').readline
from pprint import pprint
from itertools import combinations
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
max_power = 0

power_difference = 0xffffff

all_people = list(range(N))
start_list = list(combinations(all_people, len(all_people)//2))

for start_team in start_list:
    start_team_power = 0
    link_team_power = 0

    link_team = list(range(N))
    for person in start_team:
        link_team.remove(person)

    start_Snerge = list(combinations(start_team, 2))
    link_Snerge = list(combinations(link_team, 2))

    for i, j in start_Snerge:
        start_team_power += (board[i][j] + board[j][i])

    for i, j in link_Snerge:
        link_team_power += (board[i][j] + board[j][i])    
    temp = abs(link_team_power - start_team_power)

    if power_difference > temp:
        power_difference = temp
print(power_difference)