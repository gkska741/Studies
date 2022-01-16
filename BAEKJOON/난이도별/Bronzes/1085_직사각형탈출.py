import sys
sys.stdin = open('input.txt')

x, y, w, h = map(int, input().split())

distances = [w-x, x, y, h-y]
print(min(distances))