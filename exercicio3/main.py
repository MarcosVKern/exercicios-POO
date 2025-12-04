from models.funcionario_clt import Funcionario_clt
from models.funcionario_terceirizado import Funcionario_terceirizado
from models.funcionario_comissionado import Funcionario_comissionado

funcionario_clt = Funcionario_clt("André Silva", 1350)
funcionario_terceirizado = Funcionario_terceirizado("Dalva das Neves", 120, 10)
Funcionario_comissionado = Funcionario_comissionado("Maria Flores", 7000, 15)

def relatorio(funcionario):
    print(f"\nNome: {funcionario.nome}\nSalario: R$ {funcionario.calcular_salario():.2f}\n")

relatorio(funcionario_clt)
relatorio(funcionario_terceirizado)
relatorio(Funcionario_comissionado)