# Beecrowd 2304
# Solução: Mariana Ramires

i, n = map(int, input().split())
d = i
e = i
f = i

for i in range(n):
    ope = input().split()
    if ope[0] == 'C':
        if ope[1] == 'D':
            d -= int(ope[2])
        if ope[1] == 'E':
            e -= int(ope[2])
        if ope[1] == 'F':
            f -= int(ope[2])
    if ope[0] == 'V':
        if ope[1] == 'D':
            d += int(ope[2])
        if ope[1] == 'E':
            e += int(ope[2])
        if ope[1] == 'F':
            f += int(ope[2])
    if ope[0] == 'A':
        if ope[1] == 'D':
            d += int(ope[3])
            if ope[2] == 'E':
                e -= int(ope[3])
            if ope[2] == 'F':
                f -= int(ope[3])
        if ope[1] == 'E':
            e += int(ope[3])
            if ope[2] == 'D':
                d -= int(ope[3])
            if ope[2] == 'F':
                f -= int(ope[3])
        if ope[1] == 'F':
            f += int(ope[3])
            if ope[2] == 'E':
                e -= int(ope[3])
            if ope[2] == 'D':
                d -= int(ope[3])

print(d,e,f)