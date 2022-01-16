import sys
sys.stdin = open('3143_input.txt')

TC = int(input())

for i in range(TC):
    full_word, word = input().split()

    counts = full_word.count(word)
    value = len(full_word) - counts * (len(word)) + counts
    print(f'#{i+1} {value}')



