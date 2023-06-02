'''Nesse código é feito a subtração de todos os valores até chegar a 2000 (insento) e aplicado impostos em cada valor
que não é insento. Ou seja, de 3000, é retirado 2000 (insento) e aplicado o imposto apenas em 1000.
em 4500 é retirado 3000 e aplicado o imposto correspondente, sobra 1000, aplica-se novamente e soma.'''

salario = float(input())
if (salario>=0) and (salario<=2000):
    print("Isento")
elif (salario>2000.01) and (salario<=3000):
    conta = (salario - 2000) * 0.08
    print(f"R$ {conta:.2f}")
elif (salario>3000) and (salario<=4500):
    conta = (salario - 3000) * 0.18 + (1000 * 0.08)
    print(f"R$ {conta:.2f}")
elif (salario>4500):
    conta = (salario - 4500) * 0.28 + (1500 * 0.18) + (1000 * 0.08)
    print(f"R$ {conta:.2f}")
