'''para ser um triangulo retangulo é necessário pitagoras'''

a = int(input())
b = int(input())
c = int(input())

if (a**2) == (b**2) + (c**2) or (b**2) == (c**2) + (a**2) or (c**2) == (a**2) + (b**2):
    print("O triângulo é retângulo.")
else:
    print("O triângulo não é retângulo.")
