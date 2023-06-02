#O matemático alemão Gottfried Leibniz desenvolveu o seguinte método para aproximar o valor de π: π4=1−13+15−17+... Escreva um programa que permita ao usuário especificar o número de iterações usadas em esta aproximação e que exibe o valor resultante.

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