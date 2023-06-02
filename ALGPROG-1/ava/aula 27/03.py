#Um experimento científico padrão consiste em deixar cair uma bola e ver a que altura ela salta após o quique, ou seja, após o toque no solo. Depois de quicar, é determinado um índice de "quicamento" que consiste da razão entre a distância que a bola sobe após o quique e a distância da bola até o chão antes do quique. Por exemplo, se uma bola largada de uma altura de 10 metros, quica, e sobe 6 metros após o quique, o índice é de 0,6 e a distância total percorrida pela bola é de 16 metros após o quique. Se a bola continuar quicando, a distância após duas quicadas seria 10 metros + 6 metros + 6 metros + 3,6 metros = 25,6 metros. Observe que a distância percorrida para cada salto sucessivo é a distância inicial do momento em que a bola começa a retornar até o chão mais 0,6 dessa distância, que corresponde à distância que atingirá após o quique. Escreva um programa que permita ao usuário inserir a altura inicial a partir do qual a bola é solta e o número de vezes que a bola pode continuar saltando. A saída deve ser a distância total percorrida pela bola.

alturaInicial = float(input())
quicamento = float(input())
numQuiques = int(input())


