class Musica:
    def __init__(self, cantor, musica, duracao):
        self.cantor = cantor
        self.musica = musica
        self.duracao = duracao
    
    def __str__(self):
        return

minha_musica = Musica('WS', 'Juras de Amor', '3min28s')
print(f'Meu cantor é : {minha_musica.cantor}, a música é {minha_musica.musica}, a duração é {minha_musica.duracao}') 