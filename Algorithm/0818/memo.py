def fact(n):
    table[0] = 1
    for i in range(1, n+1):
        table[i] = i* table[i-1]

    return table[n]

n = int(input())

table = [0]*(n+1)

print(fact(n))