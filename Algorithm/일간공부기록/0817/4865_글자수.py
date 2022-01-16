TC = int(input())

for i in range(TC):
    str1 = input()
    str2 = input()

    max_count = 0
    for test in str1:
        temp = 0
        for index in range(len(str2)):
            if str2[index] == test:
                temp += 1
        if temp >= max_count:
            max_count = temp
        else:
            pass
    print(f'#{i+1} {max_count}')
