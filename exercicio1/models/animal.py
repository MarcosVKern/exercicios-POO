from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    @abstractmethod
    def emitir_som(self):
        pass