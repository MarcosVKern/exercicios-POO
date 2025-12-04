from .animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, raca):
        super().__init__(nome, raca)

    def emitir_som(self):
        return "Au au!"