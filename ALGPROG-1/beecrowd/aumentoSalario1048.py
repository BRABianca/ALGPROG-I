salario = float(input())
if (salario>0) and (salario<=400):
    aumento = salario * 1.15
    reajuste = aumento - salario
    percentual = "15 %"
    print(f"Novo salario: {aumento:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
elif (salario>400) and (salario<=800):
    aumento = salario * 1.12
    reajuste = aumento - salario
    percentual = "12 %"
    print(f"Novo salario: {aumento:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
elif (salario>800) and (salario<=1200):
    aumento = salario * 1.1
    reajuste = aumento - salario
    percentual = "10 %"
    print(f"Novo salario: {aumento:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
elif (salario>1200) and (salario<=2000):
    aumento = salario * 1.07
    reajuste  = aumento - salario
    percentual = "7 %"
    print(f"Novo salario: {aumento:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
elif (salario>2000):
    aumento = salario * 1.04
    reajuste = aumento - salario
    percentual = "4 %"
    print(f"Novo salario: {aumento:.2f}")
    print(f"Reajuste ganho: {reajuste:.2f}")
    print(f"Em percentual: {percentual}")
