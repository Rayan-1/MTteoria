def entrada(input_string):
    tape = list(input_string)
    tape.append(' ')

    state = 'q0'
    head = 0

    while True:
        symbol = tape[head]

        if state == 'q0':
            if symbol == '0':
                tape[head] = 'X'
                head += 1
                state = 'q0'
            elif symbol == '1':
                tape[head] = 'X'
                head += 1
                state = 'q0'
            elif symbol == '#':
                tape[head] = '#'
                head += 1
                state = 'q1'
            else:
                return False

        elif state == 'q1':
            if symbol == '0':
                tape[head] = '0'
                head += 1
                state = 'q1'
            elif symbol == '1':
                tape[head] = '1'
                head += 1
                state = 'q1'
            elif symbol == 'X':
                tape[head] = 'X'
                head += 1
                state = 'q1'
            elif symbol == ' ':
                state = 'q2'
            else:
                return False

        elif state == 'q2':
            if symbol == ' ':
                return True
            else:
                return False

# Função que verifica se uma string está na linguagem
def verifica_linguagem(input_string):
    if entrada(input_string):
        return "A entrada está na linguagem."
    else:
        return "A entrada não está na linguagem."

# Exemplo de uso
input_string = input("Digite a string para verificar se está na linguagem: ")
resultado = verifica_linguagem(input_string)
print(resultado)
