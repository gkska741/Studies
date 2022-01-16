import sys
sys.stdin = open('input.txt')

def perm(k, M):
    if k == M:
        string = ' '.join(map(str, arr))
        print(string)
        return 

    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            arr.append(i)
            visited[i] = 0
            
            perm(k+1, M)
            arr.pop()
            

N, M  = map(int, input().split())
lst = list(range(1, N+1))
visited = [0] * (N+1)
arr = []
perm(0, M)



