'''Leia a hora inicial, minuto inicial, hora final e minuto final de um jogo. A seguir calcule a duração do jogo.
Obs: O jogo tem duração mínima de um (1) minuto e duração máxima de 24 horas.'''

hi, mi, hf, mf = map(int, input().split())

if hi == hf and mi == mf:
    horas = 24
    minutos = 0
else:
    horas = hf - hi
    minutos = mf - mi
    if minutos < 0:
        minutos += 60
        horas -= 1
    if horas < 0:
        horas += 24

print(f"O JOGO DUROU {horas} HORA(S) E {minutos} MINUTO(S)")