from .venda import Venda

class Venda_prazo(Venda):
    def __init__(self, numero, valor, numero_parcela, taxa_juros_totais):
        super().__init__(numero, valor)
        self.numero_parcelas = numero_parcela
        self.taxa_juros_totais = taxa_juros_totais

    def exibir_venda(self):
        return f"Numero: {self.numero}\
            \nValor: R$ {self.valor:.2f}\
            \nNumero de parcelas: {self.numero_parcelas}\
            \nTaxa de juros: {self.taxa_juros_totais}%\
            \nParcela: R$ {self.calcular_parcelas():.2f}\n"

    def calcular_parcelas(self):
        return (self.valor + (self.valor * (self.taxa_juros_totais/100)))/self.numero_parcelas