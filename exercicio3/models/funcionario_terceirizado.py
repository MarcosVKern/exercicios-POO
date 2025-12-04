from .funcionario import Funcionario

class Funcionario_terceirizado(Funcionario):
    def __init__(self, nome, valor_diaria, dias_contratados):
        super().__init__(nome)
        self.valor_diaria = float(valor_diaria)
        self.dias_contratados = dias_contratados

    def calcular_salario(self):
        return self.valor_diaria * self.dias_contratados