import sys
sys.stdin = open('5099_input.txt')

TC = int(input())

for case_number in range(1, TC+1):
    S, num_pizza = map(int, input().split())

    pizzas = list(map(int, input().split()))
    pizzas.insert(0, 0)
    Q = [0] * S
    for i in range(S):
        Q[i] = pizzas[i]

    print(pizzas)
    print(S)




