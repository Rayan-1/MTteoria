class MaquinaTuring:
    def __init__(self, estados, alfabeto, branco, estado_inicial, estado_aceitacao, estado_rejeicao, transicoes):
        self.estados = estados
        self.alfabeto = alfabeto
        self.branco = branco
        self.estado_inicial = estado_inicial
        self.estado_aceitacao = estado_aceitacao
        self.estado_rejeicao = estado_rejeicao
        self.transicoes = transicoes
        self.fitat = [branco]
        self.cabeca = 0
        self.estado_atual = estado_inicial

    def executar(self, entrada):
        self.fitat = [self.branco] + list(entrada) + [self.branco]
        self.cabeca = 1
        self.estado_atual = self.estado_inicial

        while self.estado_atual != self.estado_aceitacao and self.estado_atual != self.estado_rejeicao:
            simbolo_atual = self.fitat[self.cabeca]
            if (self.estado_atual, simbolo_atual) not in self.transicoes:
                break
            proximo_estado, simbolo_escrito, direcao_movimento = self.transicoes[(self.estado_atual, simbolo_atual)]
            self.fitat[self.cabeca] = simbolo_escrito
            if direcao_movimento == 'E':
                self.cabeca -= 1
            elif direcao_movimento == 'D':
                self.cabeca += 1
            self.estado_atual = proximo_estado

        return self.estado_atual == self.estado_aceitacao

# Definindo estados, símbolos e funções de transição
estados = {'q0', 'q1', 'q2', 'q3', 'q4'}
alfabeto = {'0', '1', '#', 'X', '_'}
branco = '_'
estado_inicial = 'q0'
estado_aceitacao = 'q3'
estado_rejeicao = 'q4'
transicoes = {
    ('q0', '0'): ('q1', 'X', 'D'),
    ('q0', '1'): ('q1', 'X', 'D'),
    ('q0', '#'): ('q2', '#', 'S'),
    ('q1', '0'): ('q1', '0', 'D'),
    ('q1', '1'): ('q1', '1', 'D'),
    ('q1', '#'): ('q2', '#', 'S'),
    ('q2', '#'): ('q3', '#', 'S'),
    ('q1', '_'): ('q4', '_', 'S'),
    ('q2', '_'): ('q4', '_', 'S'),
    ('q0', '_'): ('q3', '_', 'S')
}

# Criar uma instância da Máquina de Turing
mt = MaquinaTuring(estados, alfabeto, branco, estado_inicial, estado_aceitacao, estado_rejeicao, transicoes)

# Solicitar entrada ao usuário
entrada = input("Digite a string para verificar se está na linguagem: ")

# Executar a Máquina de Turing na entrada fornecida
resultado = mt.executar(entrada)

# Exibir o resultado
if resultado:
    print("A entrada está na linguagem.")
else:
    print("A entrada não está na linguagem.")
