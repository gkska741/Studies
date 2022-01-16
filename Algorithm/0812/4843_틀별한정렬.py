TC = int(input())

def special_sort(lst):
    length = len(lst)
    new_list = []


#    length = 10
#    0 1 2 3 4 5 6 7 8 9
#    9 0 8 1 7 2 6 3
#
    for i in range(length):
        if i % 2 == 0:
            index = length-1 - int(i/2)
            new_list.append(str(lst[index]))
        if i % 2 == 1:
            index = i - int((i+1)/2)
            new_list.append(str(lst[index]))
    string = ''
    for i in range(10):
        string += new_list[i] + ' '
    return string



def sorting(lst):
    n = len(lst)
    for i in range(n-1):
        for j in range(n-1):
            if lst[j] > lst[j+1]:
                lst[j+1], lst[j] = lst[j], lst[j+1]
            else:
                pass
    return lst

result = []
for i in range(TC):
    N = int(input())
    sequence = list(map(int, input().split()))
    sequence = sorting(sequence)
    answer = special_sort(sequence)
    result.append(answer)

for i in range(len(result)):

    print(f'#{i+1} {result[i]}')