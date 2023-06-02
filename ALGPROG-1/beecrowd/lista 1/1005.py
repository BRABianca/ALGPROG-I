# Leia 2 Nes de ponto flutuante de dupla precisão A e B, que correspondem a 2 notas de um aluno.
A = int(input())
B = int(input())
MEDIA = (A * 3.5 + B * 7.5)
print("MEDIA = {:.5f}".format(MEDIA / 11))