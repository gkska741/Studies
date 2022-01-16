import sys
sys.stdin = open('input.txt')

'''

1666 2666 3666 4666 5666 6661 6662 6663 6664 6665 6666 6667 6668...

'''
n = int(input())
memo = []
number = 666
while len(memo) < n:
    if '666' in str(number):
        memo.append(number)
    number += 1

print(memo[-1])