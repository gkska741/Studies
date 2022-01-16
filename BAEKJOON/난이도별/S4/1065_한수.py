N = int(input())

cnt = 99
if N < 100:
    print(N)
else:
    for num in range(100, N+1):
        num = str(num)
        if 2*int(num[1]) == int(num[0]) + int(num[2]):
            cnt += 1
    print(cnt)


     
