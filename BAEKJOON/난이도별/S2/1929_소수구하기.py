M, N = map(int, input().split())

def is_prime(i):
    if i == 1:
        return False
    else:
        for j in range(2, round(i**0.5)+1):
            if i % j == 0:
                return False
        return True

for i in range(M, N+1):
    if is_prime(i):
       print(i)

    




