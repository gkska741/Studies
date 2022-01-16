#import sys
#sys.stdin = open('4880_input.txt')


arr = [0, 1, 3, 2, 1]

lose = [0, 2, 3, 1]
def play(s, e):
    if s == e:
        return s

    mid = (s + e) // 2
    l = play(s, mid)
    r = play(mid + 1, e)

    if lose[arr[l]] == arr[r]:
        return r
    return l
print(play(1, 4))









