'''Para determinar se uma cadeia de caracteres é formada apenas por dígitos numéricos, utilizamos o método isnumeric(). Projete e implemente um programa em python que leia uma cadeia de caracteres e, em seguida, determine se a cadeia lida é formada apenas por dígitos numéricos sem utilizar a função isnumeric(str).

A entrada é dada por uma cadeia de caracteres.

A saída consiste em escrever VERDADEIRO se a palavra é formada apenas por dígitos numéricos e FALSO, caso contrário.

Use os exemplos abaixo como padrão.'''

cadeia = input()

# Verificação dos dígitos numéricos
ehDigitos = True
for caractere in cadeia:
    if not '0' <= caractere <= '9':
        ehDigitos = False
        break

if ehDigitos:
    print("VERDADEIRO")
else:
    print("FALSO")