import sys
sys.stdin = open('input.txt')

n = int(input())

word_list = []
for _ in range(n):
    word_list.append(input())

word_list = list(set(word_list))
n = len(word_list)

res = []
for i in range(1, 51):
    temp = []
    for j in range(n):
        if len(word_list[j]) == i:
            temp.append(word_list[j])
    res += sorted(temp)

for i in range(len(res)):
    print(res[i])
