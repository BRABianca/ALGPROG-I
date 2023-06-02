idade_dias = int(input())
anos = idade_dias // 365
meses = (idade_dias % 365) // 30
dias = (idade_dias % 365) % 30
print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(dias))

'''
Lê-se a idade em dias e converte-se para inteiro utilizando a função int(input()).

Calcula-se o número de anos completos utilizando a divisão inteira // por 365 dias.

Calcula-se o número de meses completos restantes utilizando o operador de módulo % por 365 dias e em seguida dividindo 
por 30 dias.

Calcula-se o número de dias restantes utilizando o operador de módulo % por 365 dias e em seguida o operador de módulo 
% por 30 dias.

Imprime-se o resultado utilizando a função print() e a formatação de string para inserir os valores das variáveis anos,
 meses e dias no meio do texto.
'''