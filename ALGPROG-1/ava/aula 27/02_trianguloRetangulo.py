'''Escreva um programa que leia o comprimento de três lados de um triângulo como entrada. A saída do programa deve
indicar se o triângulo é ou não um triângulo retângulo. Lembre-se do teorema de Pitágoras que diz que em um triângulo
retângulo, o quadrado de um lado é igual à soma dos quadrados dos outros dois lados.'''

a = int(input())
b = int(input())
c = int(input())

if (a**2) == (b**2) + (c**2) or (b**2) == (a**2) + (c**2) or (c**2) == (a**2) + (b**2):
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")