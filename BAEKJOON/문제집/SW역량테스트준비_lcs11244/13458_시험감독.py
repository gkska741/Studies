input = open('input.txt').readline
import math

def func(N):
    return N - B  


N = int(input())
rooms = list(map(int, input().split()))
B, C = map(int, input().split())

answer = N
rooms = list(map(func, rooms))

for i in range(N):
    if rooms[i] > 0:
        answer += math.ceil(rooms[i]/C)

print(answer)

