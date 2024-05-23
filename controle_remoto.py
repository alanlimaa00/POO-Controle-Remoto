class ControleRemoto:
    #atributos do meu objeto
    def __init__(self, cor, tamanho, espessura):
        self.cor = cor
        self.tamanho = tamanho
        self.espessura = espessura

    #métodos do meu objeto
    def alterar_temperatura(self, botao):
        if botao == '+':
            print('Temperatura aumentada...')
        elif botao == '-':
            print('Temperatura reduzida')

meu_controle = ControleRemoto('branco', '5cm', '2cm')
print('Classe Mãe')
print(f'Cor: {meu_controle.cor}, Tamanho: {meu_controle.tamanho}, Espessura: {meu_controle.espessura}')

class ControleRemotoUniversal(ControleRemoto):
    def ligar(self):
        print('Ligando ar-condicionado')
    
    def alterar_temperatura(self, modo):
        if modo == 'resfriar':
            print('climatizando o ambiente...')
        elif modo == 'ventilar':
            print('Ventilando o ambiente')

meu_controle = ControleRemotoUniversal('preto', '4.5cm', '3cm')
print('Classe Filha')
print(f'Cor: {meu_controle.cor}, Tamanho: {meu_controle.tamanho}, Espessura: {meu_controle.espessura}')