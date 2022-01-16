input = open('input.txt').readline
from copy import deepcopy
N = int(input())

num_list = [1] * 10
num_list[0] = 0

for _ in range(N-1):
    temp_num_list = num_list[::]
    for i in range(10):
        if i == 0:
            temp_num_list[i] = num_list[i+1]
        elif i == 9:
            temp_num_list[i] = num_list[i-1]
        else:
            temp_num_list[i] = (num_list[i-1] + num_list[i+1])
    num_list = temp_num_list
print(sum(num_list)%1000000000)

