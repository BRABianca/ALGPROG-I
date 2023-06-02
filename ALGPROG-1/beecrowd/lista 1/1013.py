a, b, c = map(int, input().split())
maior_ab = (a+b + abs(a-b)) / 2
#'abs" é uma função nativa que retorna o N absoluto de um número, o N numérico sem o sinal.
maior = (maior_ab + c + abs(maior_ab - c)) / 2
print(int(maior), "eh o maior")

''' NESSE CÓDIGO, A PRIMEIRA LINHA LÊ OS TRÊS NES DE ENTRADA COMO UMA STRING E USA A FUNÇÃO 'map()' PARA 
CONVERTÊ-LOS PARA 'int'.
A SEGUNDA E A TERCEIRA LINHA CALCULAM O MAIOR N ENTRE 'a' E 'b' UTILIZANDO A FÓRMULA FORNECIDA NO ENUNCIADO. A 
QUARTA LINHA CALCULA O MAIOR N ENTRE O RESULTADO ANTERIOR E 'c'.
AA ÚLTIMA LINHA IMPRIMI O MAIOR N INTEIRO ENCONTNRADDO, SEGUIDO DA MENNSAGEM "eh o maior". 
UTILIZAMOS 'int(maior)' PARA GARANTIR QUE A SAÍDA SEJA UM NÚMERO INTEIRO.
'''
