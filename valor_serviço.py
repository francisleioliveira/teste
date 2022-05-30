from compras_telhado import Compras
class ValorServiço(Compras):
    def __init__(self, compras, ferramentas, areas, q_telha):
        super( ).__init__(compras, ferramentas, areas, q_telha)

class Valor:
    def valor1 (self):
        print(int(input('\nO Valor para fazer esse serviço é : ')))

V = Valor()
V.valor1()

