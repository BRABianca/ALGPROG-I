'''Escreva um programa em Python que faça uso de laços aninhados para imprimir o padrão abaixo. Devem ser lidos um valor inteiro N (N >= 0) que representa a quantidade de linhas a serem impressas. Observe que, a cada linha é impresso um caractere a mais do padrão.'''

N = int(input())

for i in range(N):
    for j in range(i + 1):
        print("*", end="")
    print()