# Beecrowd 3416
# Solução: Guilherme Nakazato

estudantes, litros, ml = map(int, input().split())
litros_totais = (ml * estudantes) // (litros * 1000) * litros

if (ml * estudantes) % (litros * 1000) > 0:
    litros_totais += litros

print(int(litros_totais))