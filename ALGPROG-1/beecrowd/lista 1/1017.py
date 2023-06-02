tempo_gasto = int(input())
velocidade_media = int(input())
autonomia = 12 #km/l
distancia = (velocidade_media * tempo_gasto)
gasolina = (distancia / autonomia)
print("{:.3f}".format(gasolina))