codA, A, NA = input().split()
codA = int(codA)
A = int(A)
NA = float(NA)
codB, B, NB = input().split()
codB = int(codB)
B = int(B)
NB = float(NB)
SOMA = (A*NA + B*NB)
print("N A PAGAR: R$ {:.2f}".format(SOMA))