import sys
sys.stdin = open('input.txt')


TC = int(input())

code = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
}

def shifter(n):
    res = ''
    for i in range(4):
        if n & (1 << i):
            res = '1' + res
        else:
            res = '0' + res
    return res


for case_number in range(1, TC+1):
    L, N = input().split()
    res = ''
    for i in range(int(L)):
        number = 0
        try: 
            number += int(N[i])
            res += shifter(number)
        except:
            number += int(code[N[i]])
            res += shifter(number)

    print(f'#{case_number} {res}')

            
