import sys
sys.stdin = open('input.txt')


TC = int(input())

for _ in range(TC):
    arr = list(map(int, input().split()))
    
    avg = sum(arr[1:])/arr[0]
    cnt = 0    

    for i in range(1, arr[0]+1):
        if arr[i] > avg:
            cnt += 1

    print("{:.3f}%".format(cnt * 100 /arr[0]))

    
