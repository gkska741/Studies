input = open('input.txt').readline

L, C = map(int, input().split())
words = sorted(list(input().split()))

# words = [a t c i s w]
p = ['a', 'e', 'i', 'o', 'u']

result = []

def dfs(mo, ja, pwd, pwd_len, last_idx):
    
    if mo >= 1 and ja >= 2 and len(pwd) == pwd_len:
        print(pwd)
        return
    
    for j in range(last_idx+1, C):
        if words[j] in p:
            dfs(mo+1, ja, pwd+words[j], pwd_len, j) 
        else:
            dfs(mo, ja+1, pwd+words[j], pwd_len, j) 

for i in range(C):
    if words[i] in p:
        dfs(1, 0, words[i], L, i)
    else:
        dfs(0, 1, words[i], L, i)

