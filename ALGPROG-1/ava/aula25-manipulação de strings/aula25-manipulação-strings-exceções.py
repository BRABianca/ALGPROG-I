'''acesso à string'''
# nome = "Bianca Avalos"
# print(nome[0])

'''operadores: in'''
# nome = "Bianca Avalos"
# if "B" in nome:
#     print("A letra 'B' está presente em nome.")
# else:
#     print("A letra 'B' não está presente em nome.")

'''operadores: len'''
# nome = "Bianca Avalos"
# print(len(nome))

'''cocatenação: string1 + string2'''
# nome = "Bianca"
# sobenome = "Avalos"
# nomeCompleto = nome + sobrenome
# print(nomeCompleto)

'''repetição: string * int'''
# nome = "Bianca"
# nomeRepetido = nome * 2
# print(nomeRepetido)

'''percorrendo uma string: while'''
# nome = "Bianca Avalos"
# i = 0
# while i < len(nome): 
#     print(nome[i]) #caso queira imprimir na mesma linha: print(nome[i],  end="")
#     i += 1
'''percorrendo uma string: for'''
# nome = "Bianca Avalos"
# for i in range(len(nome)):
#     print(nome[i])

'''operações: upper'''
# nome = "Bianca"
# print(nome.upper()) #string.upper()
'''operações: lower'''
# nome = "Bianca"
# print(nome.lower()) #string.lower()

'''operações: split'''
# nome = "B,i,a,n,c,a"
# print(nome.split(",")) #dia, mes, ano = input("Digite uma data: ").split("/")
'''utilizando for para iterar'''
# fila = input("Digite uma sequencia de números separados por espaço: ")
# for item in fila.split(" "):
#     print(item)

'''operações: partition'''
# antes, sep, depois = input("Digite valores: ").partition("-")
# print(antes)
# print(sep)
# print(depois)
'''utilizando while para iterar'''
# fila = input("Digite os itens da fila separados por espaço: ")
# item, sep, fila = fila.partition(" ")
# # Condição de parada é quando um item da fila for igual a zero
# while int(item) != 0:
#     print(item)
#     # Pega o próximo item da fila
#     item, sep, fila = fila.partition(" ")

'''Exercicio 1: Escreva um programa que lê uma frase e uma string
antiga e uma string nova. O programa deve imprimir uma
string contendo a frase original, mas com a última
ocorrência da string antiga substituída pela string nova.'''

# frase = input("Digite a frase: ")
# stringAntiga = input("Digite a sting antiga: ")
# stringNova = input("Digite a sting nova: ")

# partes = frase.partition(stringAntiga)

# if partes[1]:
#     novaFrase = partes[0] + stringNova + partes[2]
#     print("Nova frase:", novaFrase)
# else:
#     print("String antiga não encontrada na frase:")

''' Exercicio 2: Faça um programa que lê uma string que representa uma
cadeia de DNA e gera a cadeia complementar.'''
# cadeia_dna = input("Digite a cadeia de DNA: ")

# cadeia_complementar = ""
# for nucleotideo in cadeia_dna:
#     if nucleotideo == "A":
#         cadeia_complementar += "T"
#     elif nucleotideo == "T":
#         cadeia_complementar += "A"
#     elif nucleotideo == "C":
#         cadeia_complementar += "G"
#     elif nucleotideo == "G":
#         cadeia_complementar += "C"

# print("Cadeia complementar: ", cadeia_complementar)

'''Exercicio 3: Faça um programa que lê uma frase e retorna o número
de palavras que a frase contém. Considere que a palavra pode começar 
e/ou terminar por espaços'''
# frase = input().split()
# print(len(frase))

''' Exercicio 4: Faça um programa que lê uma frase e substitui todas as
ocorrências de espaço por "#".'''
# frase = input().split()
# for i in range(len(frase)):
#     print(frase[i], end="#")

# frase = input()
# frase_modificada = frase.replace(" ", "#")
# print(frase_modificada)

'''Tratamento de exceções: try/except'''
# print("Vamos dividir dois números inseridos po você\n")
# num1 = input("Insira o primeiro número: ")
# num2 = input("Insira o segundo número: ")

# try:
#     resultado = int(num1) / int(num2)
#     print("O resultado é " + str(resultado))
# except ZeroDivisionError: #caso queira para todos os erros, basta não definir, use apenas except.
#     print("O segundo número não pode ser zero.")
# except ValueError:
#     print("Você deve inserir dois números válidos.")