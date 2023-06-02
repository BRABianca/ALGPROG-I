# Beecrowd 3049
# Solução: Guilherme Nakazato

area_nota = 70 * 160
B = int(input())
T = int(input())

area_felix = ((B + T) * 70) / 2
area_marzia = area_nota - area_felix

if area_felix > area_nota / 2:
    print(1)
elif area_marzia > area_nota / 2:
    print(2)
else:
    print(0)