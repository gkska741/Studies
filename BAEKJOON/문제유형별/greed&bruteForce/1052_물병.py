from os import mkdir


input = open('input.txt').readline
N, K = map(int, input().split())

waterpoll = [0, N]
highest_water = 1
result = 0
while True:
    if not waterpoll[1]:
        for i in range(1, len(waterpoll)):
            if waterpoll[i] > 1:
                mok, nam = divmod(waterpoll[i], 2)
                
                if i == len(waterpoll)-1:
                    waterpoll[i] = nam
                    waterpoll.append(mok)
                else:
                    waterpoll[i] = nam
                    waterpoll[i+1] += mok

    if sum(waterpoll) != 1:
        waterpoll[1] += 1
        result += 1
    else:
        break    
    print(waterpoll)
