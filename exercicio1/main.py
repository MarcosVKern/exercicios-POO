from models.cachorro import Cachorro
from models.gato import Gato

gato = Gato("Astolfo", "Persa")
cachorro = Cachorro("Roberto", "Labrador")

def detalhes(animal):
    print(f"{animal.nome} é um {animal.__class__.__name__} da raça {animal.raca}")
    print(f"{animal.__class__.__name__}s fazem {animal.emitir_som()}")

detalhes(gato)
detalhes(cachorro)