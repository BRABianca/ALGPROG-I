'''Um biólogo local precisa de um programa para prever o crescimento populacional. As entradas são o número inicial de organismos, a taxa de crescimento (representada por um número real maior que 1), o tempo (em horas) necessárias para atingir essa taxa de crescimento e o intervalo total de tempo em que a população cresce. Por exemplo, pode-se começar com uma população de 500 organismos, uma taxa de crescimento de 2,0 e um período de crescimento de 6 horas para atingir essa taxa de crescimento. Assumindo que nenhum dos organismos morre, isso implicaria que essa população dobraria de tamanho a cada ciclo de 6 horas. Assim, após 6 horas de crescimento, teríamos 1000 organismos, e após 12 horas, teríamos 2000 organismos. Escreva um programa que receba como entradas os dados acima e mostre uma estimativa da população final após o tempo total de crescimento da população, considerando o número de ciclos de crescimento existentes dentro do tempo total informado.'''

numOrganismosInicial = int(input())
taxaCrescimento = float(input())
tempoHoras = int(input())
intervaloCrescimento = int(input())

numCiclos = intervaloCrescimento // tempoHoras

populacaoFinal = numOrganismosInicial * (taxaCrescimento**numCiclos)

print(f"A população total será de {int(populacaoFinal)}")