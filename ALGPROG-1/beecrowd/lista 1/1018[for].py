N = int(input())
notas = [100, 50, 20, 10, 5, 2, 1]
qtd_notas = [0]*7
print(N)
for i in range(7):
    qtd_notas[i] = N // notas[i]
    N = N % notas[i]

    print("{} nota(s) de R$ {},00".format(qtd_notas[i], notas[i]))