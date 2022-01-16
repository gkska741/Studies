import sys
sys.stdin = open('input.txt')

input_value = 1
while input_value != 0:
    input_value = list(map(int, input()))
    if input_value == [0]:
        break
    else:
        boolean = True
        for i in range(len(input_value)//2):
            if input_value[i] != input_value[len(input_value)-1-i]:
                print('no')
                boolean = False
                break
    if boolean == True:
        print('yes')
                

