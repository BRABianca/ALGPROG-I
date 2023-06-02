#Escreva um programa que leia uma sequência de números reais informados pelo usuário. A leitura deve ser finalizada quando o usuário pressionar a tecla <ENTER> por duas vezes consecutivas. Por fim, o programa deve imprimir a soma e a média dos números lidos, com duas casas decimais.

quantidadeNumeros = 0
soma = 0

while True:
    numeros = input()
    
    if numeros == "":
        break
    
    soma += float(numeros)
    quantidadeNumeros += 1
    
media = soma / quantidadeNumeros

print(f"A soma é: {soma:.2f}")
print(f"A média é: {media:.2f} ")