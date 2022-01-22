input = open('input.txt').readline
TC = int(input())

for _ in range(TC):
    Target = int(input())
    fibo = [1, 1]
    while fibo[-1] < 1000000000:
        fibo.append(fibo[-1] + fibo[-2])
        if fibo[-1] > Target:
            fibo.pop()
            break

    my_num = 0
    result_list = []
    while my_num != Target:
        if Target - my_num >= fibo[-1]:
            temp = fibo.pop()
            my_num += temp
            result_list.append(temp)
        else:
            fibo.pop()
    for i in range(len(result_list)-1, -1, -1):
        print(result_list[i], end=' ')
    print()