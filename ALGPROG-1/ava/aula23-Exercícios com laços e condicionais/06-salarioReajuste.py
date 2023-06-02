'''Os professores na maioria das escolas privadas são pagos de acordo com um cronograma que fornece um salário com base no número de anos de experiência docente. Por exemplo, um professor iniciante em uma dada escola pode receber R$30.000 no primeiro ano. Para cada ano de experiência após esse primeiro ano, até o limite de 10 anos, o professor recebe um aumento de 2% sobre o valor inicial. Escreva um programa que exiba uma tabela salarial para os professores desta escola. As entradas são o salário inicial, o percentual de aumento e o número de anos no cronograma. Cada linha da tabela salarial deve conter o número do ano e o salário desse ano.'''

salarioInicial = float(input())
percentualAumento = (float(input()) / 100)
anosCronograma = int(input())

print("Ano   Salário")
print("--------------")

for ano in range(anosCronograma):
    print(f"{ano + 1:2d}{salarioInicial:12.2f}")
    salarioInicial += salarioInicial * percentualAumento