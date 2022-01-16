import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())

def perm(k, M):
    global cnt 
    if k >= 2:
        if arr[-1] < arr[-2]:
            return
        else:
            if k == M:
                string = ' '.join(map(str, arr))
                print(string)
                return
    else:
        if k == M:
            string = ' '.join(map(str, arr))
            print(string)
            return

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            arr.append(i)

            perm(k+1, M)

            visited[i] = 0
            arr.pop()



lst = list(range(1, N+1))
visited = [0] * (N+1)
arr = []
cnt = 0
perm(0, M)
