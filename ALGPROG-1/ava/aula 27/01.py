'''Escreva um programa que leia o comprimento de três lados de um triângulo como entrada. A saída do programa deve
indicar se o triângulo é ou não um triângulo equilátero.'''

a = int(input())
b = int(input())
c = int(input())

if a == b == c:
    print("O triângulo é equilátero.")
else:
    print("O triângulo não é equilátero.")