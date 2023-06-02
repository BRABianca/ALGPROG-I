while True:
    try:
        # Ler a entrada como pares de inteiros de 32 bits sem sinal
        a, b = map(int, input().split())

        # Converter inteiros em representações binárias de 32 bits
        a_bits = format(a, '032b')
        b_bits = format(b, '032b')

        # Executar soma bit a bit, imitando o comportamento do carregador de bit (carry)
        result_bits = ''
        carry = '0'
        for i in range(31, -1, -1):
            if a_bits[i] == '0' and b_bits[i] == '0':
                result_bits = carry + result_bits
                carry = '0'
            elif a_bits[i] == '1' and b_bits[i] == '1':
                result_bits = carry + result_bits
                carry = '1'
            else:
                if carry == '0':
                    result_bits = '1' + result_bits
                else:
                    result_bits = '0' + result_bits

        # Imprimir resultado como um inteiro sem sinal de 32 bits
        print(int(result_bits, 2))

    except EOFError:
        break