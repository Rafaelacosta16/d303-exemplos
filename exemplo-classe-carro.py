class Carro:
   qdte_rodas = 4

    def __init__(self, cor, marca, modelo):
        self.cor = cor
        self.marca =marca
        self.modelo =modelo

        def buzinar(self):
            print('Biiiiiibiiii')

        def acelerar(self):
            print('Vrooom Vroooom')

        carro1 = Carro('vermelho', 'Ferrari', 'FF')
        carro1.buzinar()
        carro1.acelerar()

        