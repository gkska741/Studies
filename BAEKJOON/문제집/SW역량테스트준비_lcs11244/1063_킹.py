input = open('input.txt').readline

K, S, N = map(str, input().strip().split())
order_list = []
for _ in range(int(N)):
    order_list.append(input().strip())

chess_board = [[0] * 8 for _ in range(8)]
index = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

dictionary = {'B': [1, 0], 'T': [-1, 0], 'L': [0, -1], 'R': [0, 1], 'RT': [-1, 1], 'LT': [-1, -1], 'RB': [1, 1], 'LB': [1, -1]}

kr = index.index(K[0])
kc = 8 - int(K[1])

sr = index.index(S[0])
sc = 8 - int(S[1])
for order in order_list:
    new_kc = kc + dictionary[order][0]
    new_kr = kr + dictionary[order][1]

    if 0 <= new_kc < 8 and 0 <= new_kr < 8:
        
        if new_kc == sc and new_kr == sr:

            new_sr = sr + dictionary[order][1]
            new_sc = sc + dictionary[order][0]

            if 0 <= new_sc < 8 and 0 <= new_sr < 8:
                kc = new_kc
                kr = new_kr

                sc = new_sc
                sr = new_sr
        else:
            kc = new_kc
            kr = new_kr   

print(index[kr] + str(8-kc))
print(index[sr] + str(8-sc))