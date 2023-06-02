valor = int(input())
valor1 = valor
inverso = 0

while valor1>0:
    resto1 = valor1%10
    inverso = inverso*10 + resto1
    valor1 = valor1//10

if inverso == valor:
    print("É um palíndromo.")
else:
    print("Não é um palíndromo.")