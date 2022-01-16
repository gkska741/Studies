import sys
sys.stdin = open('input.txt')

TC = int(input())

for tc in range(1, TC+1):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split()))) #기준 리스트
    B = list(map(int, input().split())) #각각의 원소가 A에 들어있는지?

    cnt = 0
    for num in B:
        s = 0; e = N-1
        direction = 0
        while s <= e:
            mid = (s + e) // 2
            if A[mid] == num:
                cnt += 1
                break
            elif A[mid] < num:
                s = mid + 1
                if direction == -1:
                    break
                direction = -1
            else:
                e = mid - 1
                if direction == 1:
                    break
                direction = 1
    print(f'#{tc} {cnt}')





