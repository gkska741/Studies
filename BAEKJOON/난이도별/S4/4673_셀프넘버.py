n = 10000

result = [1] * 100001

def self_number(n):
    str_n = list(str(n))
    int_n = list(map(int, str_n))
    return n + sum(int_n)

for x in range(1, 10001):
    while x < 10000:
        x = self_number(x)
        if result[x] == 0:
            break
        result[x] = 0

for j in range(1, 10001):
    if result[j] == 1:
        print(j)
    

        
     

