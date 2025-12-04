from .funcionario import Funcionario

class Funcionario_clt(Funcionario):
    def __init__(self, nome, salario_base):
        super().__init__(nome)
        self.salario_base = float(salario_base)

    def calcular_salario(self):
        return self.salario_base - (self.salario_base * (15/100))