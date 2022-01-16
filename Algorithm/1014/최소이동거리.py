import sys; sys.stdin = open('input.txt', 'r')


for tc in range(1, int(input())+1):
    N, E = map(int, input().split())
    G = [[] for _ in range(N+1)] # 0부터 N까지의 정점 번호에 대한 공간

    for _ in range(E):
        s, e, d = map(int, input().split()) #정보 입렵받아서
        G[s].append((e, d)) #각 정점마다 어디로 갈 수있고, 그 정점까지의 가중치를 저장

    D = [0xffffff] * (N+1) # 최소값을 구할 것이기 때문에 대충 큰 값을 저장
    D[0] = 0
    
    visited = [0] * (N+1) # visited = 1의 조건 : 최단경로를 찾은 정점

    cnt = N+1

    while cnt:
        
        s,min_val = 0, 0xffffff #탐색을 시작할 초기값, 그리고 이동거리값을 정한다.

        for i in range(N+1): # 0 ~ N까지의 정점 번호에 대해서
            if visited[i] == 0 and min_val > D[i]: #아직 i정점에 대한 화실한 최단경로 설정이 안되었고, 그 정점에 대한 D[i]값이 이동거리의 최소값을 갱신한다면
                s, min_val = i, D[i] # i번째 정점을 조사하고, min_val에 D[i]를 저장한다.
        visited[s] = 1
               
        for e, d in G[s]: #s에서 출발하는 각 정점에 대해서 
            if D[e] > D[s] + d: # 더 짧은 경로값 합이 발견될 경우
                D[e] = D[s] + d # D[e]를 그 값으로 교체한다

        cnt -= 1
    print(f'#{tc} {D[N]}')