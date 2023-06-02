'''Escreva um programa que leia um número inteiro. O programa deve exibir "Positivo" se o número for maior que 0, "Negativo" se o número for menor que 0 e "Zero" se o número for igual a 0. O programa deve exibir "Par" se o número é par e “Ímpar” se o número for ímpar. A saída deve ter o formato que segue os exemplos abaixo.'''

N = int(input())

if N > 0:
    print("Positivo")
elif N == 0:
    print("Zero")
else:
    print("Negativo")

if N % 2 == 0:
    print("Par")
else:
    print("Ímpar")