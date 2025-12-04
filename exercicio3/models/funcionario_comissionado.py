from .funcionario import Funcionario

class Funcionario_comissionado(Funcionario):
    def __init__(self, nome, total_vendas, comissao):
        super().__init__(nome)
        self.total_vendas = float(total_vendas)
        self.comissao = comissao

    def calcular_salario(self):
        return self.total_vendas * (self.comissao/100)