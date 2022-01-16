input = open('input.txt').readline

from itertools import combinations
while True:
    numbers = list(map(int, input().split()))
    if numbers == [0]:
        break

    numbers.pop(0)
    perms = list(combinations(numbers, 6))

    for perm in perms:
        print(*perm)
    print()

    
    

