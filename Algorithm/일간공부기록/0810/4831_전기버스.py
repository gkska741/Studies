TC = int(input())
result = []



def mapping(start, chargelocation):
    location = []
    for i in range(start[1]+1):
        location.append('0')
    for i in chargelocation:
        location[i] = '1'
    
    return location

def calc(lst, k):
    num_of_charge = 0  
    i = 0
    while i < len(lst):
        i += k

        if i >= len(lst)-1:
            break
        elif lst[i] == '1':
            num_of_charge += 1
        else:
            while lst[i] !='1':
                i -= 1
            num_of_charge += 1

    return num_of_charge

def can_charge(lst, k):
    temp = []
    for i in range(len(lst)):
        if lst[i] == '1':
            temp.append(i)
        else:
            pass
    for j in range(len(temp)-1):
        if temp[j+1] - temp[j] > k:
            return False
    return True


for i in range(TC):

    init = list(map(int, input().split()))
    charge_location = list(map(int, input().split()))

    location = mapping(init, charge_location)


    if can_charge(location, init[0]) == False:
        result.append(0)
    else:
        num_of_charge = calc(location, init[0])
        result.append(num_of_charge)

    print(f'#{i+1} {result[i]}')