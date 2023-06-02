name = input()
salario_fixo = float(input())
total_de_vendas = float(input())
TOTAL = (salario_fixo+total_de_vendas*15/100) #AQUI TAMBÉM PODE SER 0.15
print("TOTAL = R$ {:.2f}".format(TOTAL))