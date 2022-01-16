TC = int(input())


for i in range(TC):
    word = input()
    length = len(word)
    half = length//2
    is_loop = True
    for j in range(half):
        if word[j] != word[length-j-1]:
            is_loop = False
        else:
            pass
    if is_loop == True:
        print(f'#{i+1} {1}')
    else:
        print(f'#{i + 1} {0}')


