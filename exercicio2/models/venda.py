from abc import ABC

class Venda(ABC):
    def __init__(self, numero, valor):
        self.numero = numero
        self.valor = float(valor)

    def exibir_venda(self):
        return f"Numero: {self.numero}\nValor: R$ {self.valor:.2f}\n"