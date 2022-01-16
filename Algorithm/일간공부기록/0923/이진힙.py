H = [0] * 100
hsize = 0

def isEmpty():
    return hsize == 0

def push(item):
    # 마지막 다음에 추가
    global hsize
    hsize += 1
    H[hsize] = item
    # 부모 > 자식 : 쵀대힙
    c = hsize; p = c // 2
    while p:
        if H[p] > H[c]:
            H[p], H[c] = H[c], H[p]
        else:
            break
        c = p
        p = c // 2


def pop():
    global hsize
    ret = H[1]
    H[1] = H[hsize]
    hsize -= 1
    # 부모 > 자식 대소관계 조사
    p = 1; c = 2
    while c <= hsize:
        # 오른쪽 자식이 있다면 왼쪽 자식과 비교
        if c + 1 <= hsize and H[c] < H[c + 1]:
            c += 1

        if H[p] < H[c]:
            H[p], H[c] = H[c], H[p]
        else:
            break
        p = c
        c = p * 2

    return ret


data = [7, 2, 5, 3, 4, 6]

for val in data:
    push(val)
print(H)
while hsize:
    print(pop(), end=' ')
