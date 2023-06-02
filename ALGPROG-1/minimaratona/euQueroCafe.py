N, L, D = map(int, input().split())

quantidadeMinima = N * D
LemMilitros = L * 1000

if quantidadeMinima > LemMilitros:
    calculo = (quantidadeMinima + LemMilitros) // 1000
    print(calculo)
else:
    print(quantidadeMinima // 1000)
