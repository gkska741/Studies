import sys
from typing import overload
sys.stdin = open('input.txt')

TC = int(input())

for case_number in range(1, TC+1):
    F = float(input())
    seq = ''
    res = 0
    for i in range(1, 14):
        if not F:
            break

        if i == 13:
            res = 1
            break
        
        if F - 2**(-i) >= 0 :
            seq += '1'
            F -= 2**(-i)
        else:
            seq += '0'
    if res:
        print(f'#{case_number} overflow')
    else:
        print(f'#{case_number} {seq}')


                

