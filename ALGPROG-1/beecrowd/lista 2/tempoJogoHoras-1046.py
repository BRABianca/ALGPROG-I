hi, hf = map(int, input().split())

if hi == hf:
    horas = 24
else:
    horas = hf -hi
    if horas < 0:
        horas += 24

print(f"O JOGO DUROU {horas} HORA(S)")