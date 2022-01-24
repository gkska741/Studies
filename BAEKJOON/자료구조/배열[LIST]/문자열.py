#문자열 sequence를 비교하는 4가지 방법 
# [Brute-Force, 카프-라빈, KMP, 보이어-무어]

sequence = 'TTATATTAATAAATAATTTATATTTATTATTAAATATAATAT'
key = 'TTA'

# 1. Brute_Force O(mn)

def brute_force(sequence, key):
    cnt = 0
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == key:
            cnt += 1
    return cnt

print(brute_force(sequence, key))

#KMP 알고리즘 : O(n)

#보이어-무어 알고리즘 O(n)
