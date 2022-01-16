import sys
sys.stdin = open('input.txt')

arr = [4, 5, 6, 7, 8, 9]
N = len(arr)
swap_cnt=10
visit = [set() for _ in range(swap_cnt + 1)]

ans = 0

def find_max(k):
    global ans
    val = int(''.join(map(str, arr)))

    if val in visit[k]:
        return
    visit[k].add(val)
    
    if k == swap_cnt:
        if val > ans:
            ans = val
            print(ans)

    else:
        for i in range(N-1):
            for j in range(i+1, N):
                arr[i], arr[j] = arr[j], arr[i]
                find_max(k+1)
                arr[i], arr[j] = arr[j], arr[i]
find_max(0)