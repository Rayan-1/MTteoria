def entrada(input_string):
    fita = list(input_string)
    fita.append(' ')
    #estado inicial
    state = 'q0'
    #cabeça
    head = 0

    while True:
        symbol = fita[head]
        if state == 'q0':
            if symbol == '0':
                fita[head] = 'X'
                head += 1
                state = 'q0'
            elif symbol == '1':
                fita[head] = 'X'
                head += 1
                state = 'q0'
            elif symbol == '#':
                fita[head] = '#'
                head += 1
                state = 'q1'
            else:
                return False

        elif state == 'q1':
            if symbol == '0':
                fita[head] = '0'
                head += 1
                state = 'q1'
            elif symbol == '1':
                fita[head] = '1'
                head += 1
                state = 'q1'
            elif symbol == 'X':
                fita[head] = 'X'
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
