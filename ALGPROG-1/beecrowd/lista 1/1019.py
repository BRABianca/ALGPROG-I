N = int(input())
horas = N // 3600
N = N % 3600
minutos = N // 60
N = N % 60
print("{:01d}:{:01d}:{:01d}".format(horas, minutos, N))

'''
A partir do valor de entrada, são calculados os valores de horas, minutos e segundos através de operações matemáticas 
utilizando as funções '//' (divisão inteira) e '%' (resto da divisão inteira) para obter as partes inteiras e 
fracionária do resultado.

Para obter as horas é feita a divisão inteira do valor total de segundos por 3600, que é o número de segundos em uma 
hora (3600 = 60 minutos/hora x 60 segundos/minuto), armazenado na variável 'horas'.

Para obter os minutos é feita a divisão inteira ddo valor restante (obtido através do operaddos '%' com 3600) por 60, 
que é o número de segundos em um minuto, armazenado na variável 'minutos'.

Os segundos restantes são obtidos através do operador '%' com 60, e são armazenaddo na variável 'segundos'.
 
O resultaddod é impresso 'print()' e a sintaxe de formatação de string, que permite a inserção de variáveis ddentro 
de uma string utilizanddo chaves ('{}') para indicar onde cada variável deve ser inserida.
'''