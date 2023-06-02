import sys

for line in sys.stdin:
    n = int(line)
    for i in range(n):
        message = input().strip()

        # primeira passada: desloca 3 posições para a direita na tabela ASCII
        encrypted1 = ""
        for char in message:
            if char.isalpha():
                if char.islower():
                    encrypted1 += chr((ord(char) - ord('a') + 3) % 26 + ord('a'))
                else:
                    encrypted1 += chr((ord(char) - ord('A') + 3) % 26 + ord('A'))
            else:
                encrypted1 += char

        # segunda passada: inverte a mensagem
        encrypted2 = encrypted1[::-1]

        # terceira passada: desloca 1 posição para a esquerda na tabela ASCII a partir da metade da mensagem
        half = len(message) // 2
        encrypted3 = encrypted2[:half]
        for char in encrypted2[half:]:
            if char.isalpha():
                if char.islower():
                    encrypted3 += chr((ord(char) - ord('a') - 1) % 26 + ord('a'))
                else:
                    encrypted3 += chr((ord(char) - ord('A') - 1) % 26 + ord('A'))
            else:
                encrypted3 += char

        print(encrypted3)