from telhado import Telhado


class Compras(Telhado) :
   def __init__(self, compras, ferramentas,areas,q_telha):
        super( ).__init__(compras, ferramentas)
        self.areas=areas
        self.q_telha=q_telha


compras = [ ]
compras.append('telhas')
compras.append('madeira')
compras.append('pregos')
compras.append('cimento')
ferramentas = ("martelo , serrote , trana , prumo")
areas = (int(input("Digite a área Total : ")))
q_telha= areas*20
T = Compras(compras, ferramentas, areas, q_telha)
print(T.compras,T.ferramentas,T.areas,T.q_telha)

l = len(compras)
print(l)