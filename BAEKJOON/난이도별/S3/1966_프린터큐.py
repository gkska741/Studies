input = open('input.txt').readline
TC = int(input())

for _ in range(TC):
    N, Q = map(int, input().split())

    priority = (list(map(int, input().split())))
    p_num = list(range(N))
    
    cnt = 1
    while priority:
        max_value =  max(priority)
        now_doc = priority.pop(0)
        now_num = p_num.pop(0)
        
        if not priority:
            print(cnt)
            break
            
        if now_doc >= max(priority):
            if now_num == Q:
                print(cnt)
                break
            else:
                cnt += 1
        else:
            priority.append(now_doc)
            p_num.append(now_num)


