import sys
sys.stdin = open('12397_input.txt')

TC = int(input())

def paper(L):
    global memo
    if L >= 2 and len(memo) <= L:
        memo.append(paper(L-1) + 2 * paper(L-2))
    return memo[L]

memo = [0, 1, 3]
for tc in range(TC):
    length = int(input())//10
    print(f'#{tc+1} {paper(length)}')



