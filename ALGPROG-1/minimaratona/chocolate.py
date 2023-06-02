N = int(input())
divisoes = list(map(int, input().split()))

estoque = 0
for divisao in divisoes:
    estoque += divisao - 1

print(estoque)