from models.venda_padrao import Venda_padrao
from models.venda_prazo import Venda_prazo

venda_padrao = Venda_padrao(123, 100)
venda_prazo = Venda_prazo(124, 1000, 10, 10)

print(venda_padrao.exibir_venda())
print(venda_prazo.exibir_venda())
