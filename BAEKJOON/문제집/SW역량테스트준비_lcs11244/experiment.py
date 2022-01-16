n = 15
answer = 0
clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
def solution(clothes):
    N = len(clothes)
    used = []
    comb = []
    
    def dfs(n):
        global answer
        if n == N:
            print(comb)
            answer += 1
        
        for i in range(N):
            if not i in used:
                used.append(i)
                comb.append(clothes[i])
                dfs(n+1)
                used.remove(i)
                comb.remove(clothes[i])        
        
    dfs(0)
        
    return answer
print(solution(clothes))