'''
Problema da reserva ambiental

Entrada:
1. Uma quantidade N de áreas retangulares a serem lidas.
2. Uma sequência de N conjuntos de 4 números inteiros representando as
   coordenadas que delimitam cada uma das N áreas. Os dois primeiros
   valores representam as coordenadas do canto superior esquerdo e os
   dois últimos as coordenadas do canto inferior direito.

Saída:
1. A área que corresponde à interesecção de todas as áreas lidas. 

MELHORIAS a serem implementadas:
- Ler a primeira região antes de entrar no laço while.
- Manter uma variável sentinela que interrompe o laço quando não for encontrada
  nenhuma intersecção.
'''

# Passo 1. Leitura da quantidade de áreas
areas = int(input())

# Passo 2. Inicialização das áreas com os maiores valores possíveis.
# A ideia é que os demais valores lidos sejam comparados com esses.
x1 = -1000000000
y1 = 1000000000
x2 = 1000000000
y2 = -1000000000

# Passe 3. Laço para ler as áreas e verificar a intersecção entre elas
#          duas a duas.
while (areas > 0):
    a, b, c, d = map(int, input().split())
    
    if (a > x1):
        x1 = a
    if (b < y1):
        y1 = b
    if (c < x2):
        x2 = c
    if (d > y2):
        y2 = d;
        
    areas -= 1

if (x2 < x1 or y1 < y2):
    print("nenhum")
else:
    print(x1,y1,x2,y2)