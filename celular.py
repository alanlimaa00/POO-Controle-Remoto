class Celular:
    def __init__(self, marca, modelo, cor):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
    
    def acessar_instagram(self, app):
        if app == 'instagram':
            print('Iniciando o aplicativo instagram')
        else:
            print('Acessando outra aplicação...')
        
    def __str__(self):
        return (f'Marca: {celular_alan.marca} | Modelo: {celular_alan.modelo} | Cor: {celular_alan.cor} |\n Marca: {celular_caylanne.marca} | Modelo: {celular_caylanne.modelo} | Cor: {celular_caylanne.cor}')

celular_alan = Celular('Xiaomi', 'Poco X5 Pro', 'Azul')
celular_ronney = Celular('Samsung', 'J1-Mini', 'Cinza')

class CelularGuitarrinha(Celular):
    def sistema_otimizado(self, so):
        if so == 'android':
            print('Otimizado')
        else:
            print('Inválido')

celular_caylanne = CelularGuitarrinha('Clandestina', 'Desconhecido', 'Rosa')

print(celular_alan)
print(celular_caylanne)
print(celular_ronney)