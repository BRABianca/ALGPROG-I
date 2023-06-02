areaTotal = 70 * 160
B = int(input())
T = int(input())

aFelix = ((B + T) * 70) / 2
aMarzia = areaTotal - aFelix

if aFelix > areaTotal / 2:
    print(1)
elif aMarzia > areaTotal / 2:
    print(2)
else:
    print(0)
