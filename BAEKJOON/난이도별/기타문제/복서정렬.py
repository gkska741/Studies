def solution(weights, head2head):
    N = len(weights)
    more_weight_win = [0] * N
    winrate = [0] * N
    for i in range(N):
        total = 0
        win = 0
        for j in range(N):
            
            if head2head[i][j] == 'L':
                total += 1
            if head2head[i][j] == 'W':
                total += 1
                win += 1
                if weights[i] < weights[j]:
                    more_weight_win[i] += 1
        if total != 0:
            win_total = win/total
            winrate[i] = win_total
        
    answer = list(range(1, N+1))
    change = True
    
    while change == True:
        change = False
        for i in range(N-1):
            if winrate[i] < winrate[i+1]:
                answer[i], answer[i+1] = answer[i+1], answer[i]
                weights[i], weights[i+1] = weights[i+1], weights[i]
                winrate[i], winrate[i+1] = winrate[i+1], winrate[i]       
                more_weight_win[i], more_weight_win[i+1] = more_weight_win[i+1], more_weight_win[i]   

                change = True
            elif winrate[i] == winrate[i+1]:
                if more_weight_win[i] < more_weight_win[i+1]:
                    answer[i], answer[i+1] = answer[i+1], answer[i]
                    weights[i], weights[i+1] = weights[i+1], weights[i]
                    winrate[i], winrate[i+1] = winrate[i+1], winrate[i]
                    more_weight_win[i], more_weight_win[i+1] = more_weight_win[i+1], more_weight_win[i]  
                    change = True
                elif more_weight_win[i] == more_weight_win[i+1]:
                    if weights[i] < weights[i+1]:
                        answer[i], answer[i+1] = answer[i+1], answer[i]
                        weights[i], weights[i+1] = weights[i+1], weights[i]
                        winrate[i], winrate[i+1] = winrate[i+1], winrate[i]
                        more_weight_win[i], more_weight_win[i+1] = more_weight_win[i+1], more_weight_win[i]  
                        change = True
                    elif weights[i] == weights[i+1]:
                        if answer[i] > answer[i+1]:
                            answer[i], answer[i+1] = answer[i+1], answer[i]
                            weights[i], weights[i+1] = weights[i+1], weights[i]
                            winrate[i], winrate[i+1] = winrate[i+1], winrate[i]
                            more_weight_win[i], more_weight_win[i+1] = more_weight_win[i+1], more_weight_win[i]  

                            change = True

    return answer

weights = [145,92,86]
head2head = ["NLW","WNL","LWN"]

print(solution(weights, head2head))