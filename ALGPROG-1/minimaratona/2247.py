# Beecrowd 2247
# Solução: Vinícius Lira

x=1
while True:
    n=int(input())
    if n==0:
        break
    print("Teste",x)
    c=0
    for i in range(0,n):
        a,b=input().split()
        a=int(a)
        b=int(b)
        a=a+c
        c=a-b
        print(c)
    x+=1
    print("")