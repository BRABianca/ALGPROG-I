'''O plano de crédito na NotaCoin Computer Algorithms especifica um pagamento inicial de 10% e uma taxa de juros anual de 12%. Os pagamentos mensais são de 5% do preço de compra listado, menos o pagamento inicial. Escreva um programa que receba o preço de compra como entrada. O programa deve exibir uma tabela, com cabeçalhos apropriados, de um cronograma de pagamentos durante o tempo de duração do empréstimo até zerar a dívida. Cada linha da tabela deve conter os seguintes itens:

o número do mês (começando com 1)
o saldo atual total devido
os juros devidos no mês corrente
o valor do principal devido no mês corrente
o pagamento realizado no mês corrente
o saldo restante após o pagamento
O valor dos juros de um mês é igual ao saldo* taxa / 12. O valor de o principal de um mês é igual ao pagamento mensal menos os juros devidos.'''

saldoInicial = float(input())
receita = saldoInicial * 0.05
saldoRestante = 0

print("Mês   Saldo Atual       Juros     Valor Principal        Pagamento       Saldo Restante")

for n in range(1, 21):
    if saldoInicial >= receita:
        juros = saldoInicial * 0.01
        valorPrincipal = receita - juros
        saldoRestante = saldoInicial - receita
    else:
        juros = 0
        saldoRestante = 0
        receita = saldoInicial
        valorPrincipal = saldoInicial

    print(f"{n:2d}{saldoInicial:12.2f}{juros:15.2f}{valorPrincipal:20.2f}{receita:17.2f}{saldoRestante:21.2f}")   
    saldoInicial -= receita