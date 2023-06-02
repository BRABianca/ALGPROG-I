numIteracoes = int(input())

valorPi = 0
sinal = 1
valorPiComputador = 3.141592653589793

for i in range(numIteracoes):
    valorPi = valorPi + sinal / (2*i +1)
    sinal = sinal * -1

valorPi = valorPi * 4

print(f"A aproximação de pi é {valorPi}")
print(f"Compare isso com a estimativa do computador: {valorPiComputador}")