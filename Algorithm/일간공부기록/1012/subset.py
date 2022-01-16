A, B = [], []
N = 4

def subset(k):
    if len(A) == N//2:
        print(A, B +[i for i in range(k, N)])
    elif len(B) == N//2:
        print(A + [i for i in range(k, N)], B)
    else:
        A.append(k)
        subset(k + 1)
        A.pop()

        B.append(k)
        subset(k + 1)
        B.pop()

subset(0)