# Beecrowd 2322
# Solução: Mariana Ramires

n = int(input())
sequencia = input().split()
falta = ""

for i in range(n):
    check = str(i+1)
    if check not in sequencia:
        falta = check

print(falta)