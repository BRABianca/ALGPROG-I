N = int(input()) # lê o N inteiro do arquivo de entrada

notas = [100, 50, 20, 10, 5, 2, 1] # lista com as notas disponíveis
qtd_notas = [0]*7 # inicializa uma lista com a quantidade de notas necessárias de cada tipo

print(N) # imprime o N lido

qtd_notas[0] = N // notas[0] # quantidade de notas de R$ 100
N = N % notas[0] # atualiza o N restante

qtd_notas[1] = N // notas[1] #quantidade de notas de R$ 50
N = N % notas[1] # atualiza o N restante

qtd_notas[2] = N // notas[2] # quantidade de notas de R$ 20
N = N % notas[2] # atualiza o N restante

qtd_notas[3] = N // notas[3] # quantidade de notas de R$ 10
N = N % notas[3] # atualiza o N restante

qtd_notas[4] = N // notas[4] # quantidade de notas de R$ 5
N = N % notas[4] # atualiza o N restante

qtd_notas[5] = N // notas[5] # quantidade de notas de R$ 2
N = N % notas[5] # atualiza o N restante

qtd_notas[6] = N // notas[6] # quantidade de notas de R$ 1

print("{} nota(s) de R$ 100,00".format(qtd_notas[0])) # imprime a quantidade de notas de R$ 100
print("{} nota(s) de R$ 50,00".format(qtd_notas[1])) # imprime a quantidade de notas de R$ 50
print("{} nota(s) de R$ 20,00".format(qtd_notas[2])) # imprime a quantidade de notas de R$ 20
print("{} nota(s) de R$ 10,00".format(qtd_notas[3])) # imprime a quantidade de notas de R$ 10
print("{} nota(s) de R$ 5,00".format(qtd_notas[4])) # imprime a quantidade de notas de R$ 5
print("{} nota(s) de R$ 2,00".format(qtd_notas[5])) # imprime a quantidade de notas de R$ 2
print("{} nota(s) de R$ 1,00".format(qtd_notas[6])) # imprime a quantidade de notas de R$ 1