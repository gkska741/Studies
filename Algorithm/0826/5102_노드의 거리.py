import sys
sys.stdin = open('5102_input.txt')

def bfs(Q):
    count = 1
    while Q:
        temp_Q = []
        while Q:
            index = Q.pop()
            for i in board[index]:
                if visited[i]:
                    continue
                if i == e:
                    return count
                temp_Q.append(i)

                visited[i] = 1
        count += 1
        Q = temp_Q
    return 0




TC = int(input())
for case_number in range(1, TC+1):
    V, E = map(int, input().split())
    board = [[]*(V+1) for _ in range(V+1)]
    for i in range(E):
        ns, ne = map(int, input().split())
        board[ns].append(ne)
        board[ne].append(ns)

    s, e = map(int, input().split())
    visited = [0]*(V+1)
    visited[s] = 1

    Q = [s]
    print(f'#{case_number} {bfs(Q)}')




