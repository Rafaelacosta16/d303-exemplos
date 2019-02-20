# Paradigmas de programação

class BoloLaranja:
    sabor = 'laranja'

    def __init__(self, ovos, andares):
        self.qtde_ovos = ovos
        self.qtde_andares = andares 

    def assar(self, tempo):
        print(f'O bolo de {self.qtde_andares} andares está assando por {tempo} minutos, e possui {self.qtde_ovos} ovos!')

    def servir(self):
        print('O bolo está servido!')
        
x = BoloLaranja(4, 1)
y = BoloLaranja(10, 3)
x.assar(15)


        

        