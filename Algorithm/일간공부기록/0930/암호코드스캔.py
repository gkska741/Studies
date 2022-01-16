import sys
sys.stdin = open('input.txt')


pwd = {
    (2, 1, 1): 0,
    (2, 2, 1): 1,
    (1, 2, 2): 2,
    (4, 1, 1): 3,
    (1, 3, 2): 4,
    (2, 3, 1): 5,
    (1, 1, 4): 6,
    (3, 1, 2): 7,
    (2, 1, 3): 8,
    (1, 1, 2): 9
}
def check_code():
    ans = 0
    for i in range(N):
        j = M*4 -1
        while j >= 0:
            if arr[i][j] == 1 and arr[i-1][j] == 0:
                read = []
                for _ in range(8):
                    c2 = c3 = c4 = 0
                    while arr[i][j] == 0: j -= 1
                    while arr[i][j] == 1: c4 += 1; j -= 1
                    while arr[i][j] == 0: c3 += 1; j -= 1
                    while arr[i][j] == 1: c2 += 1; j -= 1
                
                    div = min(c2, c3, c4)
                    read.append( pwd[(c2//div, c3//div, c4//div)])

                odd = read[1] + read[3] + read[5] + read[7]
                even = read[0] + read[2] + read[4] + read[6]

                if (odd * 3 + even) % 10 == 0:
                    ans += odd + even     
            j -= 1
    return ans


for tc in range(1, int(input()) +1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N)]

    for i in range(N):
        temp = input()
        for j in range(M):
            n = int(temp[j], 16)
            arr[i].append(1 if n & 8 else 0)
            arr[i].append(1 if n & 4 else 0)
            arr[i].append(1 if n & 2 else 0)
            arr[i].append(1 if n & 1 else 0)

    print(f'#{tc} {check_code()}')





