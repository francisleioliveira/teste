
from abc import ABC , abstractmethod

class Telhado(ABC):
    @abstractmethod
    def __init__(self,compras,ferramentas):
        self.compras=compras
        self.ferramentas=ferramentas
        pass