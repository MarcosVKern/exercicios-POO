from .venda import Venda

class Venda_padrao(Venda):
    def __init__(self, numero, valor):
        super().__init__(numero, valor)