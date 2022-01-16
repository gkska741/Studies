N = int(input())


lst = []
total = 0
for i in range(N):
    x = int(input())
    lst.append(x)
    total += x


lst = sorted(lst)
dic = {}
for num in lst:
    if not str(num) in dic:
        dic[str(num)] = 1
    else:
        dic[str(num)] += 1

dic = sorted(dic.items())


print(round(total/N))
print(lst[N//2])

if dic[0][1] == dic[1][1]:
    if dic[0][0] > dic[1][0]:
        print(dic[1][0])
    else:
        print(dic[0][0])
else:
    print(int(dic[0][0]))

print(max(lst)-min(lst))


