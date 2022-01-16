import sys
sys.stdin = open('input.txt')

N, A, R = map(int, input().split())
# Number of gun / Animals / Range of gun

Location = sorted(list(map(int, input().split())))

animal_location = []
for i in range(A):
    (x, y) = tuple(map(int, input().split()))
    animal_location.append((x, y))

s = 0; e = A

while s <= e:
    mid = (s+e)//2
