TC = int(input())
lst = []
for i in range(TC):
    lst.append(int(input()))

def pascal(n):
    if n == 1:
        return '1'
    elif n == 2:
        return '1 1'
    else:
        temp = pascal(n-1).split()
        result = [1]
        for i in range(1, n-1):
            result.append(int(temp[i-1]) + int(temp[i]))
        result.append(1)
        return ' '.join(list(map(str, result)))

for i in range(1, len(lst)+1):
    print(f'#{i}')
    for j in range(0, lst[i-1]):
    	print(pascal(j+1))