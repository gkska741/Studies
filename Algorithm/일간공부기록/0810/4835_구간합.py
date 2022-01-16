TC = int(input())

def PLmax(num_list, M):
    result = []
    for i in range(0, len(num_list)-M+1): 
        temp = 0
        for j in range(M): 
            temp += num_list[i+j] # i =0 -> j = 012
        result.append(temp)
    
    return max(result) - min(result)



result = []
for i in range(TC):
    NM = list(map(int, input().split()))
    num_list = list(map(int, input().split()))
    answer = PLmax(num_list, NM[1])
    result.append(answer)

for i in range(len(result)):
    print(f'#{i+1} {result[i]}')