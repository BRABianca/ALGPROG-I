'''Um número inteiro N (N > 1) cuja soma dos seus divisores, menores que ele, é menor que próprio número são chamados de números deficientes. Por exemplo, o número 8 é dito deficiente porque 8 > 1 + 2 + 4. No entanto, o número 18 não é deficiente, pois 18 <= 1 + 2 + 3 + 6 + 9.

Escreva um programa em Python que leia um número inteiro e imprima uma mensagem dizendo se ele é um número deficiente ou não, conforme exemplos abaixo.'''

N = int(input())

somaDivisores = 0
for i in range(1, N):
    if N % i == 0:
        somaDivisores += i

if somaDivisores < N:
    print(f"{N} é deficiente")
else:
    print(f"{N} não é deficiente")