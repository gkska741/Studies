import sys
from typing import final
sys.stdin = open('input.txt')

TC = int(input())


def determine(sequence):
    sequence = list(map(int, sequence))
    value = 0
    for i in range(7):
        if i % 2:
            value += sequence[i] 
        else:
            value += sequence[i] * 3
    if (value + sequence[7]) % 10 == 0:
        return sum(sequence)
    else:
        return 0



code = {
    '0001101': '0', '0011001': '1', '0010011': '2', 
    '0111101': '3', '0100011': '4', '0110001': '5',
    '0101111': '6', '0111011': '7', '0110111': '8',
    '0001011': '9'
}
for case_number in range(1, TC+1):
    C, R = map(int, input().split())
    sequence = ''
    for _ in range(C):
        barcode = input()
        if not sequence:
            if '1' in barcode:
                sequence = barcode.strip('0')
                while len(sequence) != 56:
                    sequence = '0' + sequence
    
    final_code = ''
    for s in range(0, 56, 7):
        subsequence = sequence[s:s+7]
        final_code += code[subsequence]
    res = determine(final_code)

    if res:
        print(f'#{case_number} {res}')
    else:
        print(f'#{case_number} {0}')







