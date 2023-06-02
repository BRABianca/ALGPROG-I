lanche, quantidade = map(int, input().split(" "))
if lanche == 1:
    valor = 4 * quantidade
elif lanche == 2:
    valor = 4.50 * quantidade
elif lanche == 3:
    valor = 5 * quantidade
elif lanche == 4:
    valor = 2 * quantidade
elif lanche == 5:
    valor = 1.50 * quantidade
print(f"Total: R$ {valor:.2f}")
