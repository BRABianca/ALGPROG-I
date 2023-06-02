'''Os gestores de uma empresa de gestão de trânsito planejam criar uma nova via na cidade para descongestionar as vias existentes. Para isso, eles terão de desapropriar algumas propriedades na região onde será construída a nova via. Todas as propriedades possuem terrenos no formato retangular. Eles querem escolher o melhor lugar para iniciar a construção e, para isso, têm vários locais possíveis, com diferentes dimensões de comprimento e largura. Para os gestores da empresa, o ideal é escolher o local que possua a menor área para evitar grandes desapropriações no início da obra. Eles gostariam de ter um programa de computador que, dadas as dimensões das prováveis áreas, determina o que tem menor área. Você foi contatado pela fazenda para prestar esse serviço.

A entrada do seu programa consiste de uma linha contendo um valor inteiro N, que representa o número de áreas prováveis para o início da obra. Em seguida, se programa deve ler N linhas, cada uma contendo dois números inteiros que indicam as dimensões (comprimento e largura) de cada um dos possíveis locais. As dimensões são dadas em metros. Os valores de comprimento e largura estão entre 1 e 100, incluindo esses valores (ou seja, 1 ≤ comprimento ≤ 100 e 1 ≤ largura ≤ 100).

A saída do seu programa deve ser uma linha contendo informando a área, em metros quadrados, do melhor local escolhido para a plantação de alface, conforme exemplos abaixo.'''

N = int(input())  # Lê o número de áreas prováveis

menorArea = float('inf')  # Inicializa com um valor infinito para garantir a comparação

for i in range(N):
    comprimento, largura = map(int, input().split())  # Lê as dimensões de cada área
    area = comprimento * largura  # Calcula a área da área atual

    if area < menorArea:  # Verifica se a área atual é menor que a menor área registrada
        menorArea = area

print(f"A menor área encontrada tem {menorArea} metros quadrados.")