import sys
sys.stdin = open('input.txt')


res = True
while res == True :
    lst = list(map(int, input().split()))
    if lst == [0, 0, 0]:
        res = False
    else: 
        lst = sorted(lst)
        if lst[2]**2 == (lst[1]**2 + lst[0]**2):
            print('right')
        else:
            print('wrong')


