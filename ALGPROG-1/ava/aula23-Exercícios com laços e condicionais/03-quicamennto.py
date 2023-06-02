alturaInicial = float(input())
quicamento = float(input())
numQuicadas = int(input())
distanciaTotal = 0

for i in range(numQuicadas):
    novaAltura = alturaInicial * quicamento    
    distanciaTotal = novaAltura + alturaInicial + distanciaTotal
    alturaInicial = novaAltura
print(f"A distância total aproximada percorrida pela bola é de: {distanciaTotal:.2f} unidades.")