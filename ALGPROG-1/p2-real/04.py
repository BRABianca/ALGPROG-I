'''Um coletor de mosquitos coleta mosquitos todos os dias durante N dias (0 < N < 1000). Escreva um programa que leia o valor de N (quantidade de dias) e, em seguida, uma sequência de N linhas, cada uma delas contendo o número de mosquitos coletados durante a cada dia. O programa deve imprimir a quantidade e o dia em que foi coletado o menor número de mosquitos.

OBS: Os teste consideram que não haverá repetição de quantidade de mosquitos coletados em dias distintos.'''

N = int(input())
menorQuantidade = float('inf')
diaMenorQuantidade = -1

for dia in range(1, N+1):
    quantidade = int(input())

    if quantidade < menorQuantidade:
        menorQuantidade = quantidade
        diaMenorQuantidade = dia
print(f"Foram coletados {menorQuantidade} mosquitos no dia {diaMenorQuantidade}")