m = int(input())
mesesAno = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

if m in mesesAno:
    if m in [1, 2, 3]:
        print("Primeiro Trimestre")
    elif m in [4, 5, 6]:
        print("Segundo Trimestre")
    elif m in [7, 8, 9]:
        print("Terceiro Trimestre")
    else:
        print("Quarto Trimestre")
else:
    print("Mês inválido")