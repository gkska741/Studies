import sys
sys.stdin = open('3143_input.txt')

TC = int(input())

for i in range(TC):
    full_word, word = input().split()
    full_word = list(full_word)
    word = list(word)

    index = 0
    cnt = 0
    while len(full_word) > 0:
        if full_word[0:len(word)] == word:
            for _ in range(len(word)):
                full_word.pop(0)
            cnt += 1
        else:
            full_word.pop(0)
            cnt += 1

    print(f'#{i+1} {cnt}')





