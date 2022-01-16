import sys
sys.stdin = open('input.txt', 'r')

def f(k, tries):
    #print(f'f({k}, {tries}), {tries}')
    if k == tries: #모든 시도를 통과한 경우 : 더 할 필요 x
        res = list(map(str, number))
        res = ''.join(res)
        print(f'#{case_number} {res}')
        return
    else:
        #바꿔야할 숫자: number[k], max(number: k부터 끝까지의 number)-뒤에서부터 세야 함
        if -1-k < -n: # index가 넘어가버리는 경우: 고려 x

            temp = []

            for i in range(n): #for문의 목적 : number[i]가 2개이상 있으면? temp에 index를 저장 후 서로바꿔주면 됨
                if number.count(number[i]) > 1: # 77770의 경우 7의 개수가 2개 이상 -> 7끼리 바꾸면 됨
                    j = 0
                    while len(temp) != 2:
                        if number[j] == number[i]:
                            temp.append(j)
                        j += 1
                    break
                
            if temp:
                number[temp[0]], number[temp[1]] = number[temp[1]], number[temp[0]]  #2개이상 있는 경우 : 같은숫자끼리 바꾸면 된다
            else: 
                number[-1], number[-2] = number[-2], number[-1] #모든 숫자가 서로 다른 경우 : 맨끝자리 2개만 교환하는게 가장 좋다
            f(k+1, tries)
        else: #바꿀 가치가 있는 경우(경우를 확인해야 함)
            max_val = sorted_number[-1-k] #큰 숫자(바꿔야 할 숫자)

            for index in range(n-1, -1, -1):
                if number[index] == max_val: #뒤에서부터 찾으면서 바꿔야 할 숫자를 찾음
                    break # index정보 저장

            if index != k: #두 위치가 다르면 무조건 바꾸긴 해야된다.
                res = 0
                for i in range(k+1, n-1):
                    if number[k] > number[i] and number[index] == number[index-(i-k)]: #이 경우에는 최적해가 아니기 때문에 tries + 1을 해주어야 한다.
                        res = 1
                        break
                if res:
                    tries += 1
                number[k], number[index] = number[index], number[k] #그렇지 않으면 걍 바꾸면 된다.
                f(k+1, tries)
            else: #같으면 바꿔야 할 값 = 바꿈을 당하는 값 이므로 의미가 없다. 따라서 기회를 날리므로 tries+1
                f(k+1, tries+1)

            #바꾸는게 끝나면
            pass

for case_number in range(1):
    number, tries = map(int, input().split())
    number = list(map(int, list(str(number)))) #32888 -> [3, 2, 8, 8, 8]

    n = len(number) # 5
    sorted_number = sorted(number)
    if number in [10, 100, 1000, 10000, 100000, 1000000]:
        print(-1)
    else:
        f(0, tries)

