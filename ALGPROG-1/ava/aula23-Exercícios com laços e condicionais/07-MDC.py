'''O máximo divisor comum de dois inteiros positivos, A e B, é o maior número que pode ser dividido igualmente em ambos. O algoritmo de Euclides pode ser usado para encontrar o Máximo Divisor Comum (MDC) de dois inteiros positivos. Você pode usar este algoritmo da seguinte maneira:

Calcule o resto da divisão do maior número pelo menor número.
Substitua o número maior pelo número menor e o número menor com o restante.
Repita esse processo até que o número menor seja zero.

O maior número, neste ponto, é o MDC de A e B. Escreva um programa que leia dois números inteiros e, em seguida, imprime cada etapa do processo do Algoritmo de Euclides para encontrar seu MDC.
'''
A, B = map(int, input().split(' '))

if A < B:
    A, B = B, A
while B != 0:
    restante = A % B
    A = B
    B = restante
print(f"O MDC é: {A}")

'''Amaury'''
# first, second = map(int, input().split())

# while first > 0:
#     remainder = second % first
#     second = first
#     first = remainder

# print("O MDC é:", second)