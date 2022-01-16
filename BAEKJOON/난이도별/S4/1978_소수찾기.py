import sys
sys.stdin = open('input.txt')

n = int(input())
nuM_list = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False
    return True



cnt = 0
for i in range(n):
    if is_prime(nuM_list[i]):
        cnt += 1
print(cnt)
    