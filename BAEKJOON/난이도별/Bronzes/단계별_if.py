import sys
input = sys.stdin.readline

TC = int(input())
for _ in range(TC):
    a, b = map(int, input().rstrip().split())
    print(a+b)