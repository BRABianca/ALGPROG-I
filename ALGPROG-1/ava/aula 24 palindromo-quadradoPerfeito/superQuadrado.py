#Definimos a função is_superquadrado que recebe um número n como parâmetro. A condição n >= 100 garante que o número tenha pelo menos dois dígitos consecutivos.
def is_superquadrado(n):
    while n >= 100:
        #Usamos a aritmética modular ('%') para obter o dígito anterior ('digit1') e o último dígito ('digit2') do número 'n'. Dividir por 100 e depois por 10 nos dá o dígito anterior, enquanto o resto da divisão por 10 nos dá o último dígito.
        digito1 = n % 100 // 10
        digito2 = n % 10
        #Multiplicamos o dígito anterior (digit1) por 10 e somamos com o último dígito (digit2) para formar um número de dois dígitos (num).
        num = digito1 * 10 + digito2
        #Chamamos a função 'is_quadrado_perfeito' para verificar se o número num é um quadrado perfeito. Se não for, retornamos False imediatamente, indicando que o número 'n' não é um "superquadrado".
        if not is_quadrado_perfeito(num):
            return False
        #Dividimos n por 10 para remover o último dígito e preparar o número para a próxima iteração do loop.
        n //= 10
    #Se o programa sair do loop sem retornar False, significa que todos os pares de dígitos consecutivos de n são quadrados perfeitos. Portanto, retornamos True, indicando que o número n é um "superquadrado".
    return True

#A função 'is_quadrado_perfeito' recebe um número 'num' como parâmetro e verifica se ele é um quadrado perfeito. Calculamos a raiz quadrada (raiz) de num usando a notação **. Em seguida, verificamos se o quadrado de raiz é igual a 'num'. Se for, retornamos True; caso contrário, retornamos False.
def is_quadrado_perfeito(num):
    raiz = int(num ** 0.5)
    return raiz * raiz == num

#Solicitamos ao usuário que digite um número inteiro maior que 10 e o convertemos para o tipo 'int' usando a função 'int()'.
numero = int(input())

#Chamamos a função 'is_superquadrado' passando o número digitado como argumento. Se a função retornar True, imprime-se "sim". Caso contrário, imprime-se "não".
if is_superquadrado(numero):
    print("sim")
else:
    print("não")