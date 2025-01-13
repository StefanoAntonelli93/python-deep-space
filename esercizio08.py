#  esercizio su design pattern STATE

from abc import ABC, abstractmethod
# creo classe astratta che serve da modello alle sottoclassi, non istanziabile direttamente ma dalle sottoclassi - STATE -
class StatoModulo(ABC):
    @abstractmethod
    def handle_request(self, contesto):
        pass
    
# creo sottoclassi - CONCRETE STATE -

class StatoAnalisi(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in stato di analisi dei dati.") 

class StatoRaccoltaDati(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in stato di raccolta dati.") 

class StatoStanby(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in stanby.") 

class StatoManutenzione(StatoModulo):
    def handle_request(self, contesto):
        print(f"{contesto.nome} è in manutenzione.") 
        
        
# creo classe ModuloScientifico - CONTEXT -
class ModuloScientifico:
    def __init__(self, nome):
        self.nome = nome
        self.stato = StatoStanby()
        
    def set_state(self, stato):
        self.stato = stato
    
    def request(self):
        self.stato.handle_request(self)



# creo moduli scientifici
modulo1 = ModuloScientifico("Nebula")
modulo2 = ModuloScientifico("Galileo")
modulo3 = ModuloScientifico("Celestia")

# cambio da stanby ai diversi stati e stampo i risultati

modulo1.set_state(StatoManutenzione())
modulo2.set_state(StatoAnalisi())
modulo3.set_state(StatoRaccoltaDati())

print("***")
modulo1.request()
modulo2.request()
modulo3.request()
