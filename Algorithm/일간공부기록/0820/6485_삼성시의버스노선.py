import sys
sys.stdin = open('samsungbus.txt')

TC = int(input())

for i in range(TC):

    num_of_bus = int(input())
    buses = []
    for j in range(num_of_bus):
        temp = list(map(int, input().split()))
        bus = list(range(temp[0], temp[1]+1))
        buses.append(bus)

    P = int(input())
    result = f'#{i+1} '
    for j in range(P):
        C = int(input())
        cnt = 0
        for bus in buses:
            if C in bus:
                cnt += 1
            else:
                pass

        result += f'{cnt} '

    print(result)


