'''
O código encontra a interseção entre uma interseção já encontrada e um novo retângulo lido.
Ao mesmo tempo verifica se há uma interseção, caso contrário encerra os processos de comparação
e apenas lê as coordenadas dos próximos retângulos até que o loop termine.
'''
# Quantidade de retângulos a serem lidos
N = int(input())

# Inicialização do primeiro retângulo, que por consequência será a intersecção inicial
intersec = [int(coordenada) for coordenada in input().split()]
# Variável booleana que indica se os retângulos lidos possuem intersecção
# Parte-se da premissa de que é uma afirmação verdeira
intersecExists = True

# O loop inicia em 1 porque o primeiro retângulo já foi lido acima
for i in range (1, N):
    
    # Leitura do próximo retângulo
    retangulo = [int(coordenada) for coordenada in input().split()]
    
    # Verifica se há interseção, se em algum momento não ocorreu não é mais necessário executar este trecho
    if intersecExists:
        
        # Verifica se a interseção atual e o retângulo lido possuem ou não interseção
        
        # Se a menor coordenada de um dos eixos de um dos retângulos for maior que a maior coordenada no respectivo eixo do outro retângulo estes não possuem interseção
        if (intersec[0] > retangulo[2] or retangulo[0] > intersec[2]) or (intersec[3] > retangulo[1] or retangulo[3] > intersec[1]):
            intersecExists = False
            
        # Caso contrário calcula-se as coordenadas da interseção
        else:
            # Como as coordenadas estão armazenadas em listas no formato: [X1, Y2, X2, Y1]
            # as posições 0 e 3 são as menores coordenadas do eixo X e Y respectivamente
            # analogamente as posição 1 e 2 são as maiores coordenadas do eixo Y e X respectivamente
            for j in range(4):
                if j == 0 or j == 3:
                    if intersec[j] < retangulo[j]:
                        intersec[j] = retangulo[j]
                else:
                    if intersec[j] > retangulo[j]:
                        intersec[j] = retangulo[j]

# Verifica se a interseção entre os retângulos permaneceu verdadeira

# Se verdadeiro imprime as coordenadas da interseção de todos os retângulos lidos, com 1 espaçamento após cada coordenada excluindo a última
if intersecExists:
    for i in range(4):
        print(intersec[i], end=' ' if i < 3 else '')
else:
    print('nenhum')