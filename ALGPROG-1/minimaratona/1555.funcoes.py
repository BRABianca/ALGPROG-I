N = int(input())
x, y = map(int, input().split(" "))

r = ((3*x)**2) + (y**2)
b = (2*(x**2)) + ((5*y)**2)
c = (-100*x) + (y**3)

if r > b and r > c:
    print("Rafael ganhou")
elif b > r and b > c:
    print("Beto ganhou")
else:
    print("Carlos ganhou")

''''
Modificar esse código para mostrar apenas o que obteve o
menor valor entre as funções escolhidas.
No final de todos os casos de teste, imprima quem teve
o maior valor de todos e o menor valor de todos.
'''