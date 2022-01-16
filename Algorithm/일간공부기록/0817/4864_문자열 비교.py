
TC = int(input())


for i in range(TC):
    N = input()
    M = input()
    length_N = len(N)
    length_M = len(M)

    True_False = 0
    for index in range(length_M-length_N+1):
        print(M[index:length_N+index])
        if M[index:length_N+index] == N:
            True_False = 1
        else:
            pass
    if True_False == 1:
        print(f'#{i + 1} 1')
    else:
        print(f'#{i + 1} 0')
