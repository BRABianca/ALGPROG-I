#condição de existencia de triangulo: a soma dos dois menores lados deve ser menor que o valor do maior lado.
A, B, C = map(float, input().split(" "))
if B + C > A and B - C < A:
    perimetro = A + B + C
    print(f"Perimetro = {perimetro:.1f}")
else:
    area = (A + B) * C / 2
    print(f"Area = {area:.1f}")

